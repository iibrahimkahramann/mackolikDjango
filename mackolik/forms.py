from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Kullanıcı Adı',
            'email': 'E-posta',
            'password1': 'Şifre',
            'password2': 'Şifre Tekrar',
        }

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')
        labels = {
            'username': 'Kullanıcı Adı',
            'password': 'Şifre',
        }


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Kullanıcı Adı',
            'email': 'E-posta',
            'password': 'Şifre'
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Eski Şifre",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label="Yeni Şifre",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="Yeni Şifre Tekrar",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

