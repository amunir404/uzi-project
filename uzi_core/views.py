from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.core.exceptions import PermissionDenied
from uzi_apps.accounts.utils import detectUser

from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class MustLogin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('account_login'))
        return super().dispatch(request, *args, **kwargs)

class HomePageView(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
class RegisterPartnerView(View):
    template_name = "account/register_partner.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class AppsView(TemplateView):
    pass

class AuthView(TemplateView):
    pass



partner_dashboard = AppsView.as_view(template_name="partner/dashboard.html")



class CheckAdmin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.profile.role == 'SADMIN':
            return True
        else:
            raise PermissionDenied
class CheckPartner(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.profile.role == 'PARTNER':
            return True
        else:
            raise PermissionDenied
class CheckInvestor(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.profile.role == 'INVESTOR':
            return True
        else:
            raise PermissionDenied
        
class DashboardRedirectView(MustLogin, RedirectView):
    permanent = False
    query_string = True 
    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        redirect_url = detectUser(user)
        return redirect_url

class DashboardAdminView(MustLogin,CheckAdmin, View):
    template_name = "sadmins/dashboard.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
    

class DashboardInvestorView(MustLogin,CheckInvestor, View):
    template_name = "investors/dashboard.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)