from django import forms
from .models import Post, Comentario, Tipos
from django.forms.widgets import SelectDateWidget
from datetime import datetime

class Formulario_Alta_Noticias(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'titulo',
			'tipo',
			'imagen',
			'texto',
		]

class Formulario_Actualizar_Noticias(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'titulo',
			'tipo',
			'imagen',
			'texto',
		]

class Formulario_Comentario(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = [
			'texto',
		]

class Formulario_Categoria(forms.ModelForm):
	class Meta:
		model = Tipos
		fields = [
			'tipo',
		]