from django.shortcuts import render
from scaner.forms.ip import IPRange
from scaner.utils import scan_ip_range

def scan_view(request):
    result = None
    if request.method == 'POST':
        form = IPRange(request.POST)
        if form.is_valid():
            start_ip = form.cleaned_data['start_ip']
            end_ip = form.cleaned_data['end_ip']
            result = scan_ip_range(start_ip, end_ip)
    else:
        form = IPRange()

    return render(request, 'scanner/scan.html', {'form': form, 'result': result})
