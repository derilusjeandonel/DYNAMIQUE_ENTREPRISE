from django.shortcuts import render

# Create your views here.
from .models import Client, Vendeur

def espace_utilisateur(request):
    clients = Client.objects.all()
    vendeurs = Vendeur.objects.all()

    context = {
        'clients': clients,
        'vendeurs': vendeurs,
    }
    return render(request, 'espace_utilisateur.html', context)


def home(request):
    return render(request, 'base.html')  

def Acceuil(request):
    return render(request, 'Acceuil.html')