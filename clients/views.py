from django.shortcuts import render, redirect
from notifications.mail import *
from .forms import ContactForm
from django.http import HttpResponse
from .tokens import contact_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.utils import translation
from django.utils.translation import gettext_lazy as _

registration_page = "index.html"


def register(request, lang):
    translation.activate(lang)
    form = ContactForm()

    # for key in form.fields:
        # form.fields[key].label = _(form.fields[key].label)

    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.cleaned_data['origin'] = 'web'
            record = form.save()
            record.save()
            try:
                current_site = get_current_site(request)
                email_context = {
                    'id': record.id,
                    'name': record.name,
                    'code': record.code,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(record.pk)),
                    'token': contact_activation_token.make_token(record)
                }
                to_email = record.email
                # send email from notification module as subject configured
                send_email_template(
                    email=to_email, context=email_context,
                    notification_type='customer_registration',
                    notify_on="form_submit", request=request)
                return redirect('/litigation/' + lang + '?success=true')
            except Exception as error:
                print("Print error: ", error)
                return HttpResponse(error)

    context = {"language": lang, 'form': form}
    return render(request, registration_page, context)


def activate(request, uidb64, token):
    """
        Contact activation
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        contact = Customer.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Customer.DoesNotExist):
        contact = None

    if contact is not None:
        contact.is_active = True
        contact.save()

        # START: SEND EMAIL ON CUSTOMER ACTIVATION
        # make context with record_id data dictionary
        data = Customer.objects.filter(id=contact.id).values()
        context = list(data)[0]  # from queryset -> [{}] -> {}
        # update context with name
        context['name'] = contact.name

        # check for scheduled e-mail notification on contact activation
        send_email_template(
            email=None, context=context, notification_type='customer_registration',
            notify_on="url_click", request=request
        )
        # END
        return HttpResponse(_('Data Verification Thank You'))
    else:
        return HttpResponse(_('Invalid Link'))
