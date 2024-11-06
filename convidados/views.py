from django.shortcuts import render, redirect
from django.http import HttpResponse
from noivos.models import Convidados, Presentes

# Create your views here.
def convidados(request):
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)
    presentes = Presentes.objects.filter(reservado=False).order_by('-importancia')
    return render(request, 'convidados.html', {'convidado': convidado, 'presentes': presentes})

def responder_presenca(request):
    resposta = request.GET.get('resposta')
    token = request.GET.get('token')
    convidados = Convidados.objects.get(token=token)

    if resposta not in ['C', 'R']:
        return redirect(f'/convidados/?token={token}')
    
    convidados.status = resposta
    convidados.save()


    return redirect(f'/convidados/?token={token}')

def reservar_presente(request, id):
    token = request.GET.get('token')
    convidados = Convidados.objects.get(token=token)
    presente = Presentes.objects.get(id=id)

    presente.reservado=True
    presente.reservado_por = convidados
    presente.save()


    return redirect(f'/convidados/?token={token}')