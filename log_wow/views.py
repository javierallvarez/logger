from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db import IntegrityError

# Create your views here.



'''El usuario logeado podrá ver una lista de todos los usuarios registrados
colocados por su id del más al menos reciente. Así cada nuevo usuario verá 
su foto en primer lugar.'''
def index(request):
    return render(request, "log_wow/index.html",{
        "profiles": Profile.objects.all().order_by('-id'),
    })



'''Comprueba si los datos de login introducidos son correctos,
en caso contrario decuelve un mensaje de error.'''
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "log_wow/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "log_wow/login.html")



'''El usuario sale de su cuenta y es redirigido a la página principal
donde puede ver un mensaje de "Not signed in" y el logo de bienvenida'''
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



'''En el formulario de registro se requieren campos pertenecientes a
los modelos User y Profile, los cuales están conectados para
su posterior uso una vez hecho el login'''
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        avatar = request.POST["avatar"]
        if password != confirmation:
            return render(request, "log_wow/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            form = ProfileForm(request.POST, request.FILES)
            profile = form.save(commit=False)
            profile.avatar = avatar
            profile.last_name = last_name
            profile.first_name = first_name
            profile.email = email
            profile.save()
        except IntegrityError:
            return render(request, "log_wow/register.html", {
                "message": "Username already taken.",               
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "log_wow/register.html")
        


