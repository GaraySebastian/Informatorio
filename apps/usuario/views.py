from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .forms import Formulario_Alta_Usuario
from django.urls import reverse_lazy


# Create your views here.

def registro(request):
	return render(request, 'registro.html')

class Alta_Usuario(CreateView):
	model = 'Usuario'
	form_class = Formulario_Alta_Usuario
	template_name = 'registro.html'
	success_url = reverse_lazy('noticias:principal')