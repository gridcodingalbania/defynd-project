from litigations.models import *
from clients.models import *
from django.utils.translation import gettext_lazy as _



class EmailNotification(models.Model):
    """ Email notificaions will be sent depending on type:
            - on customer registration from public form
            - on litigation form submited.
        If per each type is configured more than one email notification, 
        all templates will be sent as separate emails to the list of email receivers.

        If customer is registered and this list is configured, an email will be sent 
        as a joint of recipients.
    """

    def get_all_fields():
        """ module fields per choice: 
            - customer
            - litigation
            return:
                model fields as possible variables in jinja template message field
        """
        all_fields = ""
        enter = "\n\n"
        customer = "Customer: " + enter
        litigation = "Litigation: " + enter

        customer_all_fields = ["name"] + ["domain"] + ["uid"] + ["token"]
        customer_all_fields += [f.name for f in Customer._meta.fields]
        # name is calculated field, won't show in model fields as it is not saved in db
        customer += str(customer_all_fields) + enter

        litigation_all_fields = [f.name for f in Litigation._meta.fields] + ["domain"]
        litigation += str(litigation_all_fields) + enter

        all_fields = customer + litigation
        return all_fields

    name = models.CharField(_("Notifications"), max_length=256, )
    email_from = models.CharField(_("e-mail"), max_length=256, )
    recipients = models.CharField(_("Recipients"), max_length=256, blank=True, null=True,
                                  help_text=_("Separate with; for more than one email. If left blank, \
                     the model email will be used"))
    notification_type = models.CharField(_("Notifications Type"),
                                         choices=((None, ''),
                                                  ('customer_registration', _('Customer Registration')),
                                                  ('litigation_form', _('Litigation Form')),
                                                  ), max_length=21, default=None, )
    notify_on = models.CharField(_("Notifications On"),
                                 choices=(('form_submit', _("Form Send")),
                                          ('url_click', _("Click On Url")),
                                          ), max_length=21, default='form_submit', )
    subject = models.CharField(_("Subject"), max_length=256, null=True)
    message = models.TextField(_("Message"), null=True)
    possible_variables = models.TextField(_("Possible Variables"), null=True,
                                          help_text=_("Used In Message Field"),
                                          default=get_all_fields, )

    class Meta:
        db_table = "email_notification"
        verbose_name = _('Email Notification')
        verbose_name_plural = _('Email Notifications')


class OutgoingMailServer(models.Model):
    server = models.CharField(_("Server Host"), max_length=64, )
    port = models.CharField(_("Port"), max_length=8, )
    security_type = models.CharField(_("Security Type"),
                                     choices=((None, ''),
                                              ('TLS', 'TLS'),
                                              ('SSL', 'SSL')), max_length=10, default=None, blank=True, null=True)
    user = models.CharField(_("User"), max_length=64, blank=True, null=True)
    password = models.CharField(_("Password"), max_length=36, blank=True, null=True)

    # TODO: add a test_connection button in interface

    class Meta:
        db_table = "outgoing_mail_server"
        verbose_name = _('Outgoing Mail Server')
        verbose_name_plural = _('Outgoing Mail Server')
