from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistroClienteForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.




def registro_cliente(request):
    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)  # Autenticar al usuario después de registrarse
            return redirect('home')  # Redirige al home después del registro
    else:
        form = RegistroClienteForm()
    return render(request, 'crm/registro.html', {'form': form})


def ingreso_usuario(request):

    if request.method == 'GET':
        return render(request, 'crm/login.html', {
            'form': AuthenticationForm()
        })

    else:
        # Autenticar al usuario con el username y password proporcionado
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is not None:
            # Si la autenticación es correcta, iniciar sesión y redirigir
            login(request, user)
            return redirect('/vav/catalogo')
        else:
            # Si la autenticación falla, mostrar un error
            return render(request, 'crm/login.html', {
                'form': AuthenticationForm(),
                'error': 'Invalid username or password'
            })
