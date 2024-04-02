from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from uzi_core.views import CheckAdmin, CheckInvestor, CheckPartner

# Create your views here.
class InvestorDashboardView(LoginRequiredMixin,CheckInvestor,View):
    template_name = "investors/dashboard.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)