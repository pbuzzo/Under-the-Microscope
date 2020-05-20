from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsrModel


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UsrModel
        fields = ('username', 'email', 'bio', 'url', 'age')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UsrModel
        fields = ('username', 'email')
