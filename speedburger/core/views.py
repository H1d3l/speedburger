from django.shortcuts import render
from django.views.generic import ListView
from .models import *


# Create your views here.

class HamburguerListView(ListView):
    def get(self,request):
        hamburguer_list = Hamburguer.objects.all()
        return render(request,'hamburguer/hamburguer_list.html',{'hamburguer_list':hamburguer_list})    


class ComboHamburguerListView(ListView):
    def get(self,request):
        combo_hamburguer = ComboHamburguer.objects.all()
        return render(request,'hamburguer/combo_hamburguer_list.html',{'combo_hamburguer':combo_hamburguer})    

