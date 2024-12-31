from django import forms

class IPRange(forms.Form):
    start_ip = forms.GenericIPAddressField(label="Start IP")
    end_ip = forms.GenericIPAddressField(label="End IP")
