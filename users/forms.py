from django import forms

# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserMasterTable


class CustomUserRegisterForm(forms.Form):
    class Meta:
        model = UserMasterTable
        fields = ('username', 'e_mail', 'password')

    def is_valid(self):
        pass

    def save(self):
        pass


class CustomUserLoginForm(forms.Form):
    class Meta:
        model = UserMasterTable
        fields = ('e_mail', 'password')

    def login(self):
        pass


class CustomUserChangeDetailsForm(forms.Form):
    class Meta:
        model = UserMasterTable
        fields = ('username', 'e_mail', 'password')

    def save(self):
        pass
