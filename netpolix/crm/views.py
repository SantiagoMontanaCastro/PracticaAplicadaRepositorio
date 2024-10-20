from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistroClienteForm
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

