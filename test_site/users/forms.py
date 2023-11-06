from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(attrs={"class": "forms-input"}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={"class": "forms-input"}))


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2']
        labels = {
            'email': 'E-mail',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email
