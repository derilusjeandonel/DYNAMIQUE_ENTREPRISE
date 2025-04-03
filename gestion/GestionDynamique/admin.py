from django.contrib import admin

# Register your models here.
from .models import Vendeur, Client, Produit, Achat

admin.site.register(Vendeur)
admin.site.register(Client)
admin.site.register(Produit)
admin.site.register(Achat)