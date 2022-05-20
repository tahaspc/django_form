from django.contrib import admin

# Register your models here.
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'roll_no',
                    'phone_number', 'departments', 'is_webd', 'is_gd', 'is_ma', 'is_ui', 'is_ve', 'comments')
