from django.contrib.auth.decorators import login_required
from django.db import models
from apps.usuario.models import Usuario
from ckeditor.fields import RichTextField
from django.utils.text import slugify



class Tipos(models.Model):
	tipo = models.CharField(max_length = 50)
	def __str__(self):
			return self.tipo

class Post(models.Model):
	username = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	titulo = models.CharField(max_length = 100)
	tipo = models.ForeignKey(Tipos, on_delete=models.CASCADE)
	fecha = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)
	imagen = models.ImageField(upload_to = 'imagenes')
	texto = RichTextField('Texto')
	class Meta:
		db_table="post"
		ordering = ['-fecha']

	def __str__(self):
		return self.titulo


class Comentario(models.Model):
	username = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	fecha = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)
	texto = models.TextField()

	def __str__(self):
		return self.texto