from django.contrib import admin

from .models import User, Lead, Contact_Rep, UserProfile

admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Contact_Rep)
admin.site.register(UserProfile)
