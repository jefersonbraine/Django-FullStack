from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        nome_presente = request.POST.get('nome_presente')
        preco = request.POST.get('preco')
        importancia = int(request.POST.get('importancia'))
        foto = request.FILES.get('foto')

        if importancia < 1 or importancia > 5:
            return redirect('home')
        return HttpResponse('teste')