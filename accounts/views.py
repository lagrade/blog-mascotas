from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView

from accounts.forms import LoginForm, UserRegisterForm, UserUpdateForm


# class RegistroUsuario(CreateView):
#     model = User
#     template_name = 'accounts/registro.html'
#     form_class = RegistroUsuarioForm
#     success_url = '/accounts/perfil'


def registro_usuario(request):
    if request.method == "POST":
        form= UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/accounts/perfil')
    form = UserRegisterForm()
    contexto={
        "form":form
    }
    return render(request, "accounts/registro.html", contexto)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario=data.get('username')
            contrasenia= data.get('password')

            user = authenticate(username=usuario, password= contrasenia)

            if user:
                login(request, user)

        return redirect('/accounts/perfil')
    else:
        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})



@login_required
def pagina_perfil(request):
    return render(request, 'accounts/perfil.html')


def usuario_logueado(request):
    return {'usuario_logueado': request.user}

@login_required
def editar_request(request):
    user = request.user
    if request.method == "POST":

        form = UserUpdateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.last_name = data["last_name"]
            user.save()
            return redirect("perfil")

    form = UserUpdateForm(initial={"email": user.email, "last_name": user.last_name})
    contexto = {
        "form": form
    }
    return render(request, "/accounts/editar_perfil.html", contexto)