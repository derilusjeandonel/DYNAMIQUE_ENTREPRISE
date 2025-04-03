from django.db import models

# Create your models here.
class Vendeur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adresse = models.TextField()
    telephone = models.CharField(max_length=15)
    logo_entreprise = models.ImageField(upload_to='media/logos/')

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='media/clients/', blank=True, null=True)
    vendeur = models.ForeignKey(Vendeur, on_delete=models.CASCADE, related_name='clients_recu')

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom

class Achat(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='achats')
    produits = models.ManyToManyField(Produit, related_name='achats')
    date_achat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Achat de {self.client.prenom} {self.client.nom} le {self.date_achat}"

