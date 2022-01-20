from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField(default=True)
    is_contact_rep = models.BooleanField(default=False)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    
    def __str__(self):
        return self.user.username
    

# Lead form Model
LEAD_STATUS = {
    ('NEW', 'NEW'),
    ('OPEN', 'OPEN'),
    ('IN PROGRESS', 'IN PROGRESS'),
    ('OPEN DEAL', 'OPEN DEAL'),
    ('UNQUALIFIED', 'UNQUALIFIED'),
    ('ATTEMPTED TO CONTACT', 'ATTEMPTED TO CONTACT'),
    ('CONNECTED', 'CONNECTED'),
    ('BAD TIMING', 'BAD TIMING '),
}

SOURCE_CHOICES = {
    ('INSTAGRAM', 'INSTAGRAM'),
    ('GOOGLE SEARCH', 'GOOGLE SEARCH'),
    ('TWITTER', 'TWITTER'),
    ('REFERRAL', 'REFERRAL'),
}


class Contact_Rep(models.Model):
    # Associates 1 user to 1 Contact Rep
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10, default=None)
    last_contacted = models.CharField(max_length=50, default='01-31-2022')
    lead_status = models.CharField(choices=LEAD_STATUS, blank=True, max_length=100)
    source_of_lead = models.CharField(choices=SOURCE_CHOICES, max_length=100, blank=True)
    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True)
    # set value of for foreign key to be null. Does not delete both lead and contact
    contact_rep = models.ForeignKey("Contact_Rep", null=True, blank=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
def post_user_created_signal(sender, instance, created, **kwargs):
    if not created:
        return
    UserProfile.objects.create(user=instance)
post_save.connect(post_user_created_signal, sender=User)