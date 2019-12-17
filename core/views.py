from django.shortcuts import render, redirect
from core.models import Evento
from django.http import HttpResponse

# Create your views here.
# def index(request):
#   return redirect('/agenda/')

def lista_eventos(request):
  #usuario = request.user
  #evento = Evento.objects.filter(usuario=usuario)
  evento = Evento.objects.all()
  dados = {'eventos':evento}
  return render(request, 'agenda.html', dados)