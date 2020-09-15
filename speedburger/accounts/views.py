from django.shortcuts import render,redirect,HttpResponse
from django.views.generic.base import View
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import RegisterUserProfile

# Create your views here.
class RegisterUserProfileView(View):

    template_name = 'tela_de_registro.html'

    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        form = RegisterUserProfile(request.POST)
        if form.is_valid():
            dados_form = form.cleaned_data
            usuario = User.objects.create_user(username = dados_form['username'],
                                          email = dados_form['email'],
                                          password = dados_form['password'])

            account = UserProfile(username = dados_form['username'],
                            phone = dados_form['phone'],
                            user = usuario)

            account.save()
            return HttpResponse("Usuario criado")#ajeitar aki

        return render(request,self.template_name,{'form':form})