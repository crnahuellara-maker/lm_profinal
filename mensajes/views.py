from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm

@login_required
def inbox(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user)
    return render(request, "inbox.html", {
        "mensajes": mensajes
    })

@login_required
def enviar_mensaje(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect("inbox")
    else:
        form = MensajeForm()

    return render(request, "enviar.html", {
        "form": form
    })
