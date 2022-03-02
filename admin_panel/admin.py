from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from django.urls import path

# TODO: every staff member could see the report?? Change with dedicated permissions


class CustomAdminSite(AdminSite):
    # TODO: django administration custom site_header is not updated!
    # + 'Django site admin'
    # changed temporary for demo purposes at: 
    # env/Lib/site-packages/django/contrib/admin/templates/admin/base_site.html

    # live:
    # /opt/bitnami/python/lib/python3.8/site-packages/django/contrib/admin/templates/admin/base_site.html

    site_title = _('Litigation Management System')
    site_header = _('DEFYND')
    index_title = _('Litigation Management System')


admin_site = CustomAdminSite()


# Change Site header and title
admin.site.site_header = "Litigation Management System"
admin.site.index_title = "Litigation Management System"
admin.site.site_title = "DEFYND"
admin.site.header = "DEFYND"