
from django.urls import reverse
import uuid
def detectUser(user):
    if user.profile.role == 'PARTNER':
        redirectUrl = reverse('partner_dashboard')
        return redirectUrl
    elif user.profile.role == 'INVESTOR':
        redirectUrl = reverse('investor_dashboard')
        return redirectUrl
    elif user.profile.role == 'SADMIN':
        redirectUrl = reverse('admin_dashboard')
        return redirectUrl
    elif user.profile.role == None and user.is_superadmin:
        redirectUrl = '/admin'
        return redirectUrl
    

def generate_ref_code():
    code = str(uuid.uuid4().replace("-",""))[:12]
    return code