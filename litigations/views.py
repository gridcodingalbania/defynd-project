from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from .forms import LitigationForm
from decimal import Decimal
from notifications.mail import *
from django.utils import translation
from django.utils.translation import gettext_lazy as _


# add euro inputs here to dismiss Decimal Value Errors.
__currency_variables = ["initial_estimation_value", "target_value", "aboveground_quantification", "enrollment_amount", "IMU_final_declaration", "contract_fee", "residual_rent", "reclamation_cost"]


def litigation_view(request, lang):
    # reload_data()
    translation.activate(lang)
    context = {"language": lang}
    form = LitigationForm()
    context["form"] = form

    if request.method == "POST":
        print("testing")
        request.POST = __updateCurrencyValues(request.POST)
        request.POST = calculateResidualSurface(request.POST)
        if True:
            context["form"] = LitigationForm(request.POST)
            form = context["form"]
            print(form.is_valid())
            print(form.errors)
            if form.is_valid():
                # save the form data to model & update origin
                record = form.save()
                record.origin = 'web'

                # get client
                email = form.cleaned_data['email']
                customer = Customer.objects.filter(email=email)
                # record.client = customer and customer[0] or False
                if customer:
                    record.client = customer[0]
                record.save()
                try:
                    context = form.cleaned_data
                    context['id'] = record.id
                    context['name'] = record.name
                    current_site = get_current_site(request)
                    context['domain'] = current_site.domain
                    # send email from notification module
                    send_email_template(
                        email=None, context=context,
                        notification_type='litigation_form',
                        notify_on="form_submit",
                        request=request)

                except Exception as error:
                    print("Print error: ", error)
                    return f'    {error}'
                return redirect('/'+'litigation/'+lang+'?success=true', {"language": lang, "message": _("Thank you for your litigation, we will contact you soon!") ,"form": form})
            # TODO: redirect to completion thank you form 
            # return redirect("/thanks")
            # else:
            #     # return form with entered data, display messages at the top
            #     messages.error(request, form.errors)
    return render(request, "litigation_page.html", context)

# TODO


def __updateCurrencyValues(post_form):
    temp = post_form.copy()
    for currency_variable in __currency_variables:
        if currency_variable in temp:
            if temp[currency_variable] == "":
                temp[currency_variable] = 0
            else:
                temp[currency_variable] = __removeCommas(temp[currency_variable])
    return temp


def calculateResidualSurface(post_form):
    temp = post_form.copy()
    print(temp['surface_directly_concerned'])
    if temp['surface_directly_concerned'] and temp['occupied_area']:
        surface_directly_concerned = Decimal(temp['surface_directly_concerned'])
        occupied_area = Decimal(temp['occupied_area'])
        if surface_directly_concerned > 0 and occupied_area > 0:
            if surface_directly_concerned > occupied_area:
                temp['residual_surface'] = surface_directly_concerned - occupied_area
    return temp

# def calculateRevenue(post_form):
#     subtraction = post_form.copy()
#     if subtraction['revenue'] and subtraction['total_cost']:
#         revenue = Decimal(subtraction['revenue'])
#         total_cost = Decimal(subtraction['total_cost'])
#         if revenue > 0 and total_cost > 0:
#             if revenue > total_cost:
#                 subtraction['turnover_margin'] = revenue - total_cost
#     return subtraction


def __removeCommas(form_variable):
    splited_values = form_variable.split(",")
    string_number = "".join(splited_values)
    number = Decimal(string_number)
    return number


@property
def revenueValue(self):
    if(self.revenue != None):
        turnover_margin = revenue - total_cost
        return turnover_margin