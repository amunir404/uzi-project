from django.contrib import admin
from .models import Profile, SocialMedia, PersonalDetail,Partner,Verification
from mptt.admin import MPTTModelAdmin
admin.site.register(Profile)
admin.site.register(SocialMedia)
admin.site.register(PersonalDetail)
admin.site.register(Verification)
admin.site.register(Partner,MPTTModelAdmin)
