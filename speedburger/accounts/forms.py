from django import forms
from django.forms import utils
from django.contrib.auth.models import User

class RegisterUserProfileForm(forms.Form):

    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    adress = forms.TextInput()

    def is_valid(self):
        valid = True
        if not super(RegisterUserProfileForm, self).is_valid():
            self.adiciona_erro('Por favor verifique os dados')
            valid = False

        user_exists = User.objects.filter(username = self.cleaned_data['username']).exists()
        if user_exists:
            self.adiciona_erro('Usuario Existente')
            valid = False
        return valid


    def adiciona_erro(self, msg):
       errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,
                                        forms.utils.ErrorList())
       errors.append(msg)