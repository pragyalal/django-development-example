import django import forms
import django.contrib.auth.models import User
import basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput())

    class Meta():
        model = user
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model= UserProfileInfo
        fields=('portfolio_site','profile_pic')
