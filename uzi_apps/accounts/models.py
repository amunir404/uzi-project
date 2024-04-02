from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from mptt.models import MPTTModel, TreeForeignKey
from phonenumber_field.modelfields import PhoneNumberField
from .utils import generate_ref_code


class Profile(models.Model): 
    class Role(models.TextChoices):
        INVESTOR = "INVESTOR", "INVESTOR"
        PARTNER = "PARTNER", "PARTNER"
        SADMIN = "SADMIN", "SADMIN"
        
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.INVESTOR)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    displayname = models.CharField(max_length=20, null=True, blank=True)
    aboutme = models.TextField(null=True, blank=True)
    status_online = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.user)
    
    @property
    def name(self):
        if self.displayname:
            name = self.displayname
        else:
            name = self.user.username 
        return name
    
    @property
    def avatar(self):
        try:
            avatar = self.image.url
        except:
            avatar = static('images/avatar.svg')
        return avatar


class SocialMedia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="socialmedia")
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    tiktok = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    
class PersonalDetail(models.Model):
    class Identity(models.TextChoices):
        IDCARD = "IDCARD", "KTP"
        PASSPORT = "PASSPORT", "PASSPORT"
        DRIVING_LICENSE = "DRIVING_LICENSE", "DRIVING LICENSE"
        
    class Gender(models.TextChoices):
        MALE = "MALE", "MALE"
        FAMALE = "FAMALE", "FAMALE"
        
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="personaldetail")
    if_display = models.BooleanField(default=True)
    fullname = models.CharField(max_length=100, null=True, blank=True)
    id_number = models.BigIntegerField(null=True, blank=True)
    id_type = models.CharField(max_length=20, choices=Identity.choices, default=Identity.IDCARD,null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=Gender.choices,null=True, blank=True)
    country = models.CharField(max_length=20,null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    postal = models.CharField(max_length=100,null=True, blank=True)
    address = models.CharField(max_length=100,null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
class Verification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="verification")
    verified = models.BooleanField( default=False)
    last_updated = models.DateTimeField(auto_now=True)

class BankDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100)
    bank_account = models.BigIntegerField()
    bank_address = models.CharField(max_length=100)
    swift_code = models.BigIntegerField(blank=True, default=0)
    bank_name = models.CharField(max_length=100)


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.BigIntegerField()
    

class Partner(MPTTModel):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    user_profile = models.OneToOneField(Profile, related_name='userprofile', on_delete=models.CASCADE)
    partner_name = models.CharField(max_length=50)
    partner_description = models.TextField()
    partner_logo = models.ImageField(upload_to='partner_logo/', null=True, blank=True)
    partner_code = models.CharField(max_length=100,unique=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_approved = models.BooleanField(default=False)
    partner_website = models.CharField(max_length=100, null=True, blank=True)
    partner_facebook = models.CharField(max_length=100, null=True, blank=True)
    partner_twitter = models.CharField(max_length=100, null=True, blank=True)
    partner_instagram = models.CharField(max_length=100, null=True, blank=True)
    partner_linkedin = models.CharField(max_length=100, null=True, blank=True)
    partner_tiktok = models.CharField(max_length=100, null=True, blank=True)
    partner_youtube = models.CharField(max_length=100, null=True, blank=True)
    partner_whatsapp = models.CharField(max_length=100, null=True, blank=True)
    partner_email = models.CharField(max_length=100, null=True, blank=True)
    partner_phone = models.CharField(max_length=100, null=True, blank=True)
    partner_address = models.CharField(max_length=100, null=True, blank=True)
    partner_city = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.partner_name
    
    class MPTTMeta:
        order_insertion_by = ['partner_name']
        
    @property
    def avatar(self):
        try:
            avatar = self.partner_logo.url
        except:
            avatar = static('images/avatar.svg')
        return avatar
