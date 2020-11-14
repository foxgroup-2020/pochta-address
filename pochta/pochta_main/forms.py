from django import forms
from .models import Organisation


class ProfileForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput())
    # inn = forms.CharField(widget=forms.TextInput())
    # kpp = forms.CharField(widget=forms.TextInput())
    # second_name = forms.CharField(widget=forms.TextInput())
    # first_name = forms.CharField(widget=forms.TextInput())
    # middle_name = forms.CharField(widget=forms.TextInput())
    # email = forms.EmailField(widget=forms.EmailInput())
    # phone = forms.CharField(widget=forms.TextInput())
    # old_password = forms.CharField(widget=forms.PasswordInput())
    # new_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Organisation
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())