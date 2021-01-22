from django import forms
from .models import RegisterModel


class LoginForm(forms.Form):

    login = forms.CharField(min_length=6, max_length=20, label='Логин')
    password = forms.CharField(min_length=6, label='Пароль')


# class RegisterForm(forms.Form):
#
#     login = forms.CharField(min_length=6, max_length=20, label="Логин")
#     name = forms.CharField(max_length=20, label="Имя")
#     surname = forms.CharField(max_length=20, label="Фамилия")
#     password = forms.CharField(min_length=6, label="Пароль")


class RegisterForm(forms.ModelForm):
    print(123)

    class Meta:
        model = RegisterModel
        fields = ('login', 'name', 'surname', 'password')
