from .models import Partner
from django.conf import settings

def get_partner(request): 
    try:
        partner = Partner.objects.get(user=request.user)
    except:
        partner = None
    return dict(partner=partner)