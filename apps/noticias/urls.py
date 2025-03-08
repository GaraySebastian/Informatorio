from django.urls import path, include

from apps.noticias.views import *
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.principal, name="principal"),
    path('listar/', views.ListarPost.as_view(), name="listar"),
    path('crear/', views.crear, name="crear"),
    path('modificar/<int:pk>/', views.Modificar.as_view(), name="modificar"),
    path('eliminar/<int:pk>/', views.Eliminar.as_view(), name="eliminar"),
    path('<int:pk>/', views.noticia, name='noticia'),
]