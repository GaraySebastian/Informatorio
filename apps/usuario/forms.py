from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class Formulario_Alta_Usuario(UserCreationForm):
	class Meta:
		model = Usuario
		fields = [
			'username', 
			'email', 
			'first_name', 
			'last_name', 
			'password1', 
			'password2',
		]
