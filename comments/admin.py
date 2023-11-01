from django.contrib import admin
from .models import *


# Register your models here.
class Comadmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'timedata']


admin.site.register(Comment, Comadmin)
