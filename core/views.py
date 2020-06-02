from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.


#def index(request):
#    return redirect('/agenda')


def lista_eventos(request):
    usuario = request.user
 #   evento = Evento.objects.filter(usuario=usuario) #aqui filtra pelo usuário autenticado
 #   evento = Evento.objects.get(id=1)    --- objcts.get tras um registro
    evento = Evento.objects.all()    #--- objcts.get tras um registro

    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)