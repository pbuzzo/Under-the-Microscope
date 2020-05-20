from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from microapp.models import UsrModel
from microapp.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UsrModel
    # add fields to be accessed in admin panel
    list_display = ['email', 'username', 'bio', 'url', 'age']


admin.site.register(UsrModel)
