from django.shortcuts import render
from django.views.generic.edit import *
from .models import *


# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class HamburguerCreateView(CreateView):
    model = Hamburguer
    template_name = "hamburguer_cadastro"
