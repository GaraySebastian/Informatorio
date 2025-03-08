from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('registro/', views.Alta_Usuario.as_view(), name='registro'),
]