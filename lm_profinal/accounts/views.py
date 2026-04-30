from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import ProfileForm


# 🔐 LOGIN
def login_view(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    return render(request, "login.html", {"form": form})


# 📝 REGISTRO
def signup(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, "signup.html", {"form": form})


# 🚪 LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')


# 👤 VER PERFIL
@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "profile.html", {"profile": profile})


# ✏️ EDITAR PERFIL
@login_required
def editar_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, "editar_profile.html", {"form": form})
