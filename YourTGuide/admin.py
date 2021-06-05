from django.contrib import admin
from .models import User
from .models import donar
from .models import requests1
from .models import mobs
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(donar)
admin.site.register(requests1)
admin.site.register(mobs)