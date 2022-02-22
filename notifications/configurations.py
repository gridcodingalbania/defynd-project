# OUTGOING MAIL SERVER CONFIGURATION
from .models import OutgoingMailServer
from django.conf import settings

mail_server = OutgoingMailServer.objects.all()
# take the first configuration always
outgoing_mail_server = mail_server and mail_server[0] or False

if outgoing_mail_server:
    settings.EMAIL_HOST = outgoing_mail_server.server 
    settings.EMAIL_PORT = outgoing_mail_server.port 
    settings.EMAIL_USE_TLS = bool(outgoing_mail_server.security_type == 'TLS')
    settings.EMAIL_USE_SSL = bool(outgoing_mail_server.security_type == 'SSL')
    settings.EMAIL_HOST_USER = outgoing_mail_server.user 
    settings.EMAIL_HOST_PASSWORD = outgoing_mail_server.password 
