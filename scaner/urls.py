from django.urls import path
from scaner import views

urlpatterns = [
    path('scan/', views.scan_view, name='scan'),
]
