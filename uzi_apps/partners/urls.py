from django.urls import path

from uzi_apps.partners.views import PartnerDashboardView

app_name = "partners"

urlpatterns = [
    path('dashboard/', PartnerDashboardView.as_view(), name='Dashboard'),
]