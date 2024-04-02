from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from uzi_core.views import CheckPartner

# Create your views here.
class PartnerDashboardView(LoginRequiredMixin,CheckPartner,View):
    template_name = "partners/dashboard.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)