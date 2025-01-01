from django.db import models


STATUS_CHOICES = [
    ('create', 'Ping Scan Report Created'),
    ('scanning', 'Scan Report Scanning'),
    ('finished', 'Scan Report Finished'),
    ('error', 'Scan Report Error'),
]

class PingScanReport(models.Model):
    ips = models.JSONField(default=list, blank=True)
    status = models.CharField(max_length=16, default='create')
