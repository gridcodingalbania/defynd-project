from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, F, Sum
from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.encoding import force_str
from clients.models import Customer
from costStatements.models import *
from litigations.models import Litigation
from utils.charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
from import_export.admin import ImportMixin
from django.core.exceptions import PermissionDenied
from django.template.response import TemplateResponse
from openpyxl import load_workbook


def import_sheet(self, request, *args, **kwargs):
    """ Override import_action method to import excel sheets
    """
    if not self.has_import_permission(request):
        raise PermissionDenied

    context = self.get_import_context_data()

    import_formats = self.get_import_formats()
    form_type = self.get_import_form()
    form_kwargs = self.get_form_kwargs(form_type, *args, **kwargs)
    form = form_type(import_formats,
                     request.POST or None,
                     request.FILES or None,
                     **form_kwargs)

    if request.POST and form.is_valid():
        input_format = import_formats[
            int(form.cleaned_data['input_format'])
        ]()
        import_file = form.cleaned_data['import_file']
        # first always write the uploaded file to disk as it may be a
        # memory file or else based on settings upload handlers
        tmp_storage = self.write_to_tmp_storage(import_file, input_format)

        # then read the file, using the proper format-specific mode
        # warning, big files may exceed memory
        try:
            data = tmp_storage.read(input_format.get_read_mode())
            if not input_format.is_binary() and self.from_encoding:
                data = force_str(data, self.from_encoding)
            dataset = input_format.create_dataset(data)
        except UnicodeDecodeError as e:
            return HttpResponse(_(u"<h1>Imported file has a wrong encoding: %s</h1>" % e))
        except Exception as e:
            return HttpResponse(
                _(u"<h1>%s encountered while trying to read file: %s</h1>" % (type(e).__name__, import_file.name)))

        # prepare kwargs for import data, if needed
        res_kwargs = self.get_import_resource_kwargs(request, form=form, *args, **kwargs)
        resource = self.get_import_resource_class()(**res_kwargs)

        # prepare additional kwargs for import_data, if needed
        imp_kwargs = self.get_import_data_kwargs(request, form=form, *args, **kwargs)

        # START: read excel sheet
        wb = load_workbook(filename=import_file, data_only=True)
        sheet = wb.worksheets[0]

        sheet_ranges = wb.sheetnames  # ['modello_economics']
        # first sheet (by name)
        ws = wb[sheet_ranges[0]]
        customer, litigation, hypothesis = ws['B2'].value, ws['B3'].value, ws['B4'].value

        # column depending on hypothesis
        # A cost statement could not have two hypothesis filled at the same time!
        col = 4  # "hp 1"
        if hypothesis == "hp 2":
            col = 6
        init_value = ws.cell(row=6, column=col).value
        total_value = ws.cell(row=8, column=col).value
        init_year = ws.cell(row=10, column=col).value
        expected_finish_year = ws.cell(row=11, column=col).value

        # Find configured hypothesis to link at cost statement lines:
        hypothesis_id = Hypothesis.objects.filter(name=hypothesis)
        if not hypothesis_id:
            messages.error(request, "Please configure hypothesis!")
            return redirect("/admin/costStatements/coststatement")

        # Find customer
        customer_id = [c for c in Customer.objects.all() if c.name == customer]
        if not customer_id:
            messages.error(request, "Customer does not exist!")
            return redirect("/admin/costStatements/coststatement")

        data = {
            "client": customer_id[0],
            "init_amount": init_value,
            "total": total_value,
            "init_negotiation": init_year,
            "expected_dealing_term": expected_finish_year
        }

        # Find litigation
        litigation_id = [l for l in Litigation.objects.all() if l.name == litigation]
        if litigation_id and litigation_id:
            data["litigation"] = litigation_id[0]

        # Create cost statement
        cost_statement_id = CostStatement.objects.create(**data)
        cost_statement_id.save()
        messages.success(request, "Cost statement created!")

        row_count = sheet.max_row
        # TODO: on import, log responsible user_id
        for i in range(7, row_count):
            if i not in [8, 10, 11]:  # already read values
                cost_item = ws.cell(row=i, column=1).value
                cost_value = ws.cell(row=i, column=col).value
                category = ws.cell(row=i, column=7).value

                # blank lines or titles/items without a cost will not be taken into consideration
                if not (cost_item and cost_value):
                    continue

                # find or create item
                item_id = Item.objects.filter(name=cost_item)
                item_id = item_id and item_id[0]
                if not item_id:
                    item = {
                        "name": cost_item,
                    }
                    item_id = Item.objects.create(**item)
                    item_id.save()
                    # messages.success(request, "Item `{item_id}` created!")

                if category:
                    category_id = ItemCategory.objects.filter(name=category)
                    category_id = category_id and category_id[0]
                    if not category_id:
                        category_id = ItemCategory.objects.create(**{"name": category, })
                        category_id.save()
                    item_id.category = category_id
                    item_id.save()

                # create cost statement line
                line = {
                    "item": item_id,
                    "cost_statement": cost_statement_id,
                    "value": cost_value,
                    "hypothesis": hypothesis_id[0],
                    "percentage": ws.cell(row=i, column=col - 1).value,
                }
                cost_line_id = CostStatementItem.objects.create(**line)
                cost_line_id.save()
                # messages.success(request, "Cost line {cost_line_id} created!")

        messages.success(request, "Cost statement lines imported!")
        return redirect("/admin/costStatements/coststatement")
        # END: imported cost statement excel file
    else:
        res_kwargs = self.get_import_resource_kwargs(request, form=form, *args, **kwargs)
        resource = self.get_import_resource_class()(**res_kwargs)

    context.update(self.admin_site.each_context(request))

    context['title'] = _("Import")
    context['form'] = form
    context['opts'] = self.model._meta
    context['fields'] = [f.column_name for f in resource.get_user_visible_fields()]

    request.current_app = self.admin_site.name
    return TemplateResponse(request, [self.import_template_name],
                            context)


ImportMixin.import_action = import_sheet


@staff_member_required
def get_filter_options(request):
    grouped_costs = CostStatement.objects.annotate(year=ExtractYear('time')).values('year').order_by('-year').distinct()
    options = [cost['year'] for cost in grouped_costs]
    return JsonResponse({
        'options': options,
    })


@staff_member_required
def cost_per_category_table(request, year):
    categories = ItemCategory.objects.all()
    # TODO: fix -> keep one of two lines below for db performance
    statements = CostStatement.objects.filter(time__year=year)
    costs = CostStatementItem.objects.filter(time__year=year)
    table_header = {
        'category': 'Category',
        'total': 'Total',
        # TODO: hypothesis should be dynamic
        'hypothesis_1': 'Titolare vende',
        'hypothesis_2': 'Titolare partecipa',
    }

    cost_per_category_dict = {
        'total_categories': {},  # category.name: 0.0 for category in categories
        'total_hypothesis': {},
    }

    for category in categories:
        category_cost = 0.0

        # COSTO TOTALE
        if category.code == 'TOT':
            list_of_costs = [v[0] for v in list(costs.values_list('cost_statement__total'))]
            category_cost = round(sum(list_of_costs), 2)

        # DEBITI O INVESTIMENTO/RACCOLTA RICHIESTA
        if category.code == 'DEB':
            category_cost = 0.0

        # CASH FLOW ASSORBITO NELL'ESERCIZIO
        if category.code == 'CASH':
            category_cost = 0.0

        # MARGINE LORDO
        if category.code == 'MARG':
            category_cost = 0.0

        # COSTI DIRETTI
        if category.code == 'CDIR':
            category_cost = 0.0

        # RICAVI
        if category.code == 'RIC':
            category_cost = 0.0

        # NUMERO DI CAUSE
        if category.code == 'CNO':
            # category_cost = len(set(list(costs.values_list('cost_statement')))) or 0
            category_cost = statements.count()

        # VALORE INIZIALE CAUSA
        if category.code == 'INI':
            # list_of_costs = [v[0] for v in list(costs.values_list('cost_statement__init_amount'))]
            # category_cost = round(sum(list_of_costs), 2)
            category_cost = 0.0

        cost_per_category_dict['total_categories'][category.name] = category_cost

    print("Najada print cost_per_category_dict", cost_per_category_dict)

    return JsonResponse({
        'title': f'Costs per category in {year}',
        'data': {
            'labels': list(table_header.values()),
            'datasets': [{
                'label': 'Cost (€)',
                'backgroundColor': colorPrimary,
                'borderColor': colorPrimary,
                'data': cost_per_category_dict,
            }]
        },
    })


@staff_member_required
def get_costs_chart(request, year):
    costs = CostStatement.objects.filter(time__year=year)
    # TODO: check error and prevent when total value is zero !

    grouped_costs = costs.annotate(price=F('total')).annotate(month=ExtractMonth('time')) \
        .values('month').annotate(average=Sum('total')).values('month', 'average').order_by('month')

    costs_dict = get_year_dict()

    for group in grouped_costs:
        costs_dict[months[group['month'] - 1]] = round(group['average'], 2)

    return JsonResponse({
        'title': f'Costs in {year}',
        'data': {
            'labels': list(costs_dict.keys()),
            'datasets': [{
                'label': 'Amount (€)',
                'backgroundColor': colorPrimary,
                'borderColor': colorPrimary,
                'data': list(costs_dict.values()),
            }]
        },
    })


@staff_member_required
def cost_per_customer_chart(request, year):
    costs = CostStatement.objects.filter(time__year=year)

    # Sum, Avg
    # group by clients (helped by order by) - agreggate total
    grouped_costs = costs.values('client').annotate(cost=Sum('total')).order_by('client')

    def get_customer_dict():
        customers = costs.values_list('client', flat=True)
        customer_costs = {customer: 0.0 for customer in customers}

        names = {}
        customer_ids = list(customers)
        customer_objs = Customer.objects.filter(id__in=customer_ids)
        for customer in customer_objs:
            names[customer.id] = customer.name

        # values = costs.values_list('client', 'client__name') 
        # names = {client_id:name for client_id, name in values}
        return customer_costs, names

    # get customers
    cost_per_customer, clients = get_customer_dict()
    cost_per_customer_dict = dict()
    for group in grouped_costs:
        cost_per_customer[group['client']] = round(group['cost'], 2)

    for k, v in cost_per_customer.items():
        cost_per_customer_dict[clients[k]] = v

    return JsonResponse({
        'title': f'Cost per customer in {year}',
        'data': {
            'labels': list(cost_per_customer_dict.keys()),
            'datasets': [{
                'label': 'Amount (€)',
                'backgroundColor': colorPrimary,
                'borderColor': colorPrimary,
                'data': list(cost_per_customer_dict.values()),
            }]
        },
    })


@staff_member_required
def litigation_success_chart(request, year):
    litigations = Litigation.objects.filter(time__year=year)

    return JsonResponse({
        'title': f'Litigation success rate in {year}',
        'data': {
            'labels': ['Successful', 'Unsuccessful'],
            'datasets': [{
                'label': 'Amount (€)',
                'backgroundColor': [colorSuccess, colorDanger],
                'borderColor': [colorSuccess, colorDanger],
                'data': [
                    litigations.filter(successful=True).count(),
                    litigations.filter(successful=False).count(),
                ],
            }]
        },
    })


@staff_member_required
def litigation_registration_chart(request, year):
    litigations = Litigation.objects.filter(time__year=year)
    grouped_litigations = litigations.values('registration_type').annotate(count=Count('id')) \
        .values('registration_type', 'count').order_by('registration_type')

    registration_type_dict = dict()

    for registration_type in Litigation.CHOICES:
        registration_type_dict[registration_type[1]] = 0

    for group in grouped_litigations:
        registration_type_dict[dict(Litigation.CHOICES)[group['registration_type']]] = group['count']

    return JsonResponse({
        'title': f'Litigation by registration type in {year}',
        'data': {
            'labels': list(registration_type_dict.keys()),
            'datasets': [{
                'label': 'Amount (€)',
                'backgroundColor': generate_color_palette(len(registration_type_dict)),
                'borderColor': generate_color_palette(len(registration_type_dict)),
                # TODO: add cost per hypothesis
                'data': list(registration_type_dict.values()),
            }]
        },
    })


@staff_member_required
def statistics_view(request):
    return render(request, 'statistics.html', {})
