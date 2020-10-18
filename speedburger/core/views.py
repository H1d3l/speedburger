from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from .models import *


# Create your views here.



class IndexView(ListView):

    def get(self,request):
        hamburguer_list = Product.objects.filter(type_product='Hamburguer')
        return render(request,'index.html',{'hamburguer_list':hamburguer_list})   
    


class HamburguerListView(ListView):
    def get(self,request):
        hamburguer_list = Product.objects.filter(type_product='Hamburguer')
        return render(request,'hamburguer/hamburguer_list.html',{'hamburguer_list':hamburguer_list})    


class ComboListView(ListView):
    def get(self,request):
        combo_hamburguer = Combo.objects.all()
        return render(request,'hamburguer/combo_hamburguer_list.html',{'combo_hamburguer':combo_hamburguer})    

