from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from django.urls import path

# TODO: every staff member could see the report?? Change with dedicated permissions

@staff_member_required
def admin_statistics_view(request):
    return render(request, 'admin/statistics.html', {
        'title': 'Statistics'
    })


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

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        app_list += [
            {
                'name': _('Dashboard'),
                'app_label':'dashboard',
                'models': [
                    {
                        'name':_('Statistics'),
                        'object_name': 'statistics',
                        'admin_url': '/admin/statistics',
                        'view_only': True,
                    }
                ],
            },
            # {
            #     'name': _('Translate'),
            #     'app_label': 'translate',
            #     'models': [
            #         {
            #             'name': _('Translate'),
            #             'object_name': 'rosetta',
            #             'admin_url': '/rosetta',
            #             'view_only': True,
            #         }
            #     ],
            # }
        ]
        return app_list

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('statistics/', admin_statistics_view, name='admin-statistics'),
        ]
        return urls

admin_site = CustomAdminSite()


# Change Site header and title
admin.site.site_header = "Litigation Management System"
admin.site.index_title = "Litigation Management System"
admin.site.site_title = "DEFYND"
admin.site.header = "DEFYND"