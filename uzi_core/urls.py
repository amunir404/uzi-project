"""
URL configuration for a_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from uzi_apps.accounts.views import profile_view
from uzi_core.views import HomePageView
from .views import DashboardAdminView, DashboardRedirectView, partner_dashboard, DashboardInvestorView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomePageView.as_view()),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', DashboardRedirectView.as_view(), name='dashboard'),
    path('administrator/dashboard/', DashboardAdminView.as_view(), name='admin_dashboard'),
    path('investor/dashboard/', DashboardInvestorView.as_view(), name='investor_dashboard'),
    path('partner/dashboard/', view=partner_dashboard, name='partner_dashboard'),
    path('administrator/', include('uzi_apps.sadmin.urls')),
    path('partner/', include('uzi_apps.partners.urls')),
    path('investor/', include('uzi_apps.investors.urls')),
    path('profile/', include('uzi_apps.accounts.urls')),
    
    path('@<username>/', profile_view, name="profile_user"),
]

# Only used in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)