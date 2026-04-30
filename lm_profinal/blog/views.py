from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Page
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

class PageList(ListView):
    model = Page
    template_name = "pages.html"

class PageDetail(DetailView):
    model = Page
    template_name = "detail.html"

# 🔥 CRUD

class PageCreate(LoginRequiredMixin, CreateView):
    model = Page
    fields = '__all__'
    template_name = "crear.html"
    success_url = reverse_lazy('pages')

class PageUpdate(LoginRequiredMixin, UpdateView):
    model = Page
    fields = '__all__'
    template_name = "editar.html"
    success_url = reverse_lazy('pages')

class PageDelete(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = "borrar.html"
    success_url = reverse_lazy('pages')
