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

def statistics_view(request):
    print("hello world")
    context = {'name': "ELION"}
    return render(request, 'statistics.html', context)
