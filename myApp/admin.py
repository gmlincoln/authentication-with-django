from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(User_Model)
class User_Model_Display(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'user_type')
    list_filter = ('user_type',)