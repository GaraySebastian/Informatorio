
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import *
from .forms import Formulario_Alta_Noticias, Formulario_Actualizar_Noticias, Formulario_Comentario, Formulario_Categoria
from .filters import PostFilter

class Modificar(UpdateView):
	model = Post
	form_class = Formulario_Actualizar_Noticias
	template_name = 'actualizar.html'
	success_url = reverse_lazy('noticias:principal')


	
class Eliminar(DeleteView):
	model = Post
	success_url = reverse_lazy('noticias:principal')

class ListarPost(ListView):
	model = Post
	template_name = 'listar.html'


def noticia(request, pk=None):
	post = Post.objects.get(pk = pk)
	comentario = Comentario.objects.filter(post = post).order_by('-pk')

	if request.method == "POST":
		form = Formulario_Comentario(request.POST or None)
		if form.is_valid():
			texto = request.POST.get('texto')
			comentario = Comentario.objects.create(post=post, username=request.user, texto=texto)
			comentario.save()
			return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
	else:
		form = Formulario_Comentario()

	context = {
	'noticia':post,
	'comentario':comentario,
	'form':form,
	}
	return render(request, 'noticia.html', context)


def principal(request):
	myFilter =PostFilter(request.GET, queryset=Post.objects.all())
	context = {'myFilter' : myFilter}
	return render(request, 'principal.html', context)


def crear(request):
	if request.method == "POST":
		form = Formulario_Alta_Noticias(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.username = request.user
			post.save()
			return redirect('/', pk=post.pk)
	else:
		form = Formulario_Alta_Noticias()
	return render(request, 'crear.html', {'form': form})


def comentario(request, ok):
	post =get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = Formulario_Comentario(request.POST)
		if form.is_valid():
			comentario = form.save(commit=False)
			comentario.username = request.user
			comentario.post = post
			comentario.save()
			return redirect('/', pk=post.pk)
	else:
		form = Comentario()
	return render(request, 'comentario.html', {'form': form})


def categoria(request):
	if request.method == "POST":
		form = Formulario_Categoria(request.POST)
		if form.is_valid():
			seleccion 
			seleccion= Post.filter(tipo__gte=tipo)
			return render(request, 'principal.html',{"tipos":seleccion})
	else:
		tipos = Tipos()
		context = { 'tipos' : tipos}
		return render(request, 'principal.html', context)