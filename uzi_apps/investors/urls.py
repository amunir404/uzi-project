from django.urls import path

from uzi_apps.investors.views import InvestorDashboardView

app_name = "members"

urlpatterns = [
    path('dashboard/', InvestorDashboardView.as_view(), name='Dashboard'),
]