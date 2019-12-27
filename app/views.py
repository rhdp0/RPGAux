from django.shortcuts import render, redirect
from django.urls import reverse_lazy # Funcao para redirecionar o usuario
#from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from .forms import UsersForm
from .models import Users


#home page
def main(request):
    return render(request, 'app/main.html', {})


#pagina de login
def login(request):
    return render(request, 'app/login.html', {})


# pagina de cadastro de jogador
def register(request):
    form = UsersForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'app/register.html', {'form': form})    
    

# Create your views here.
