from django.contrib import admin
from .models import UserInfo, Experience, ContactInfo

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Experience)
admin.site.register(ContactInfo)