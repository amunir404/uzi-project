from django.urls import path

from uzi_apps.sadmin.views import InvestorDetailView,InvestorListView, PartnerDetailView, PartnerListView, SAdminDashboardView

app_name = "admins"
urlpatterns = [
   path('dashboard/', SAdminDashboardView.as_view(), name='Dashboard'),
   path('accounts/investor',InvestorListView.as_view(), name='InvestorList'),
   path('accounts/investor/<pk>/',InvestorDetailView.as_view(), name='InvestorDetail'),
   path('accounts/partner',PartnerListView.as_view(), name='PartnerList'),
   path('accounts/partner/<pk>/',PartnerDetailView.as_view(), name='PartnerDetail'),
]