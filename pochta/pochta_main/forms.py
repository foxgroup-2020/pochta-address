from django import forms
from .models import FileParse

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'border',
        'style': 'font-size: 14pt; border: 1px solid black; padding:10px;',
        'placeholder': 'Имя пользователя',

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'border',
        'style': 'font-size: 14pt; border: 1px solid black; padding:10px;',
        'placeholder': 'Пароль',
    }))


class UploadFileForm(forms.ModelForm):
    file_path = forms.FileField(label='',
                                widget=forms.FileInput(attrs={
                                    'style': 'display:none;',
                                    'onchange': 'form.submit()',
                                }))

    class Meta:
        model = FileParse
        fields = ['file_path']

