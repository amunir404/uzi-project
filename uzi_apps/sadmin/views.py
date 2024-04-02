from django.shortcuts import render
from django.views import View
from uzi_apps.accounts.models import Partner
from uzi_core.views import CheckAdmin,  MustLogin
from django.views.generic.list import ListView
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import DetailView
# Create your views here.

class SAdminDashboardView(MustLogin,CheckAdmin, View):
    template_name = "sadmins/dashboard.html"

   
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class InvestorListView(MustLogin,CheckAdmin, ListView):

    template_name = "sadmins/investors/list.html"
    context_object_name = "investors"
    queryset = User.objects.filter(profile__role="INVESTOR")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["unverified"] = User.objects.filter(verification__verified=False,profile__role="INVESTOR")
        context['login_record_days'] = User.objects.filter(last_login__gte=timezone.now())
        context['login_record_30_days'] = User.objects.filter(last_login__gte=timezone.now() - timezone.timedelta(days=30))
        context['title_page'] = "Investors Manage"
        return context
    

class InvestorDetailView(MustLogin,CheckAdmin, DetailView):
    template_name = "sadmins/investors/detail.html"
    context_object_name = "investor"
    queryset = User.objects.all()
    
class PartnerListView(MustLogin,CheckAdmin, ListView):

    template_name = "sadmins/partners/list.html"
    context_object_name = "partners"
    queryset = Partner.objects.all()
    

class PartnerDetailView(MustLogin,CheckAdmin, DetailView):
    template_name = "sadmins/partners/detail.html"
    context_object_name = "investor"
    queryset = Partner.objects.all()