from django import forms
from .models import OutgoingMailServer


class ServerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = OutgoingMailServer
        fields = ('server', 'port', 'security_type', 'user', 'password',)
