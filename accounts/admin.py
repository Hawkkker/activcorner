from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Course, Registration

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'active']
    #list_display = ['name', 'start_date', 'end_date', 'view_users_link', 'active']

    #def view_users_link(self, obj):
    #    print(obj)
    #    count = obj.customuser_set.count()
    #    url = (
    #        reverse("admin:accounts_customuser_changelist")
    #        + "?"
    #        + urlencode({"courses__id": f"{obj.id}"})
    #    )
    #   return format_html('<a href="{}">{} Users</a>', url, count)

    #view_users_link.short_description = "Users"

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['course', 'user', 'canceled', 'cancel_date']

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name',]

admin.site.register(CustomUser, CustomUserAdmin)