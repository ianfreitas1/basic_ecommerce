from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'first_name', 'last_name', 'email', 'address')
    list_display = ('id', 'username', 'first_name', 'last_name', 'email')


admin.site.register(User, UserAdmin)
