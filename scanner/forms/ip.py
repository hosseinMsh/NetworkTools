from django import forms

from scanner.models import PingScanReport


class IPRange(forms.Form):
    start_ip = forms.GenericIPAddressField(label="Start IP")
    end_ip = forms.GenericIPAddressField(label="End IP")

    class Meta:
        model = PingScanReport
        fields = ['start_ip', 'end_ip']
