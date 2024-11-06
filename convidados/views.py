from django.shortcuts import render
from django.http import HttpResponse
from noivos.models import Convidados, Presentes

# Create your views here.
def convidados(request):
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)
    presentes = Presentes.objects.filter(reservado=False).order_by('-importancia')
    return render(request, 'convidados.html', {'convidado': convidado, 'presentes': presentes})