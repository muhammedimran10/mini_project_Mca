from django.contrib import admin

# Register your models here.
from users.models import Userprofile

admin.site.register(Userprofile)