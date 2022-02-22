from django.contrib import admin
from .models import EmailNotification, OutgoingMailServer
from django.utils.translation import gettext_lazy as _
from .forms import ServerForm


class EmailNotificationAdmin(admin.ModelAdmin):
    menu_title = "Notifications"
    list_display = ('name', 'notification_type', 'notify_on', 'email_from', 'recipients', 'subject')
    search_fields = ('name', 'notification_type', 'email_from', 'recipients',) 
    list_filter = ('notification_type', 'notify_on', 'email_from',)
    readonly_fields = ['possible_variables']
    fieldsets = [
        (
            None,
            {
                'fields': (('name',),
                           ('notification_type',),
                           ('notify_on',),
                           ),
            }
        ),
        (
            None,
            {
                'fields': (('email_from',),
                           ('recipients',),
                           ),
                'classes': ('wide', 'extrapretty'),
            }
        ),
        (
            None,
            {
                'fields': ('subject',),
                'classes': ('wide', 'extrapretty'),
            }
        ),
        (
            None,
            {
                'fields': ('message',),
                'classes': ('wide', 'extrapretty'),
            }
        ),
        (_("Possible Variables"),
         {
             'fields': ('possible_variables',),
             'classes': ('collapse', 'extrapretty'),
         }
         ),
    ]


class OutgoingMailServerAdmin(admin.ModelAdmin):
    menu_title = "Outgoing Mail Server"
    list_display = ('server', 'port', 'security_type', 'user', )
    form = ServerForm


admin.site.register(EmailNotification, EmailNotificationAdmin)
admin.site.register(OutgoingMailServer, OutgoingMailServerAdmin)
