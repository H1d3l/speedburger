from django import forms
from django.forms import utils
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterUserProfileForm(forms.Form):

    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    phone = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(RegisterUserProfileForm, self).is_valid():
            self.adiciona_erro('Por favor verifique os dados')
            valid = False

        user_exists = User.objects.filter(
            username=self.cleaned_data['username']).exists()
        email_exists = User.objects.filter(
            email=self.cleaned_data['email']).exists()
        phone_exists = UserProfile.objects.filter(
            phone=self.cleaned_data['phone']).exists()

        if user_exists:
            self.adiciona_erro('Desculpe,nome de usuário já existe')
            valid = False
        elif email_exists:
            self.adiciona_erro('Desculpe,email já existe')
            valid = False
        elif phone_exists:
            self.adiciona_erro('Desculpe,phone já existe')
            valid = False
        return valid

    def adiciona_erro(self, msg):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,
                                         forms.utils.ErrorList())
        errors.append(msg)
