from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['password']
