from notifications.models import *
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

# per template ne html - render_to_string()
from django.template import Context, Template


def send_email_template(request, notification_type, notify_on, email, context):
    # filter configured email notification record on type
    queryset = EmailNotification.objects.filter(
        notification_type=notification_type, notify_on=notify_on)

    print(queryset)
    # send emails for all found records
    [notify(obj, request, email_to=email, context=context) for obj in queryset]


def notify(self, request, email_to, context):
    """ 
        @self: Email Notification Object
        @email_to: Email from Form
        @context: dictionary of model fields

        @message - of type jinja template, matched with context
                    & converted in plain text
    """
    try:
        subject = self.subject
        message = self.message
        print(subject)
        print(message)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [x for x in self.recipients.split(';')] if self.recipients else []
        # recipients are from notification module if filled in configuration
        # or from registration/ litigation form
        if email_to and not recipient_list:
            print(email_to)
            recipient_list.append(email_to)

        # convert jinja template in plain text with values
        template = Template(message)
        # add context from the model form
        ctx = Context(context)
        html_content = template.render(ctx)
        
        # send mail
        message = html_content
        send_mail(
            subject,
            message,
            email_from,
            recipient_list,
            fail_silently=False,
        )
        # send_mail( subject, message, email_from, recipient_list, fail_silently=False)
        # #    fail_silently=False, html_message=message) 
        
        # TODO: make possible to render (jinja + html) format from message value
        # msg = render_to_string(html_content, context)

        # new_email = EmailMessage(
        #             subject, message, from_email=email_from, to=recipient_list
        # )
        # new_email.send()

        # TODO: catch error on duplicate contact email  
        # IntegrityError at /registration/ : UNIQUE constraint failed: customer.email

    except BadHeaderError:
        return HttpResponse(_('invalid-header-found'))

    return True
