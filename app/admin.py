from django.contrib import admin
from .models import UserFrom


# Register your models here.

@admin.register(UserFrom)
class UserFormAdmin(admin.ModelAdmin):
    pass
