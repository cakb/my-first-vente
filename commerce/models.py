from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    """presentation du produit"""
    name=models.CharField(max_length=200,verbose_name="Nom du produit")
    short_desc=models.CharField(max_length=150,verbose_name="Description courte")
    long_desc=models.TextField(verbose_name="Description longue")
    image=models.ImageField(upload_to='photo/',verbose_name="Miniature du produit",null=True)
    price=models.CharField(max_length=200,verbose_name="Prix du produit")
   
    class Meta:
        verbose_name="Produit"
        verbose_name_plural="Produits"

        def __str__ (self):
            return self.name

class Photo(models.Model):
    """les photos montrent les differents produits"""
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_photo=models.ImageField(upload_to='photo/')
   
class Order(models.Model):
    created_at = models.DateTimeField('date d\'envoi',default=timezone.now)
    contacted = models.BooleanField('demande traitée', default=False)
    contact = models.ForeignKey("Contact",on_delete=models.CASCADE,default=0)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default=0)
    class Meta:
        verbose_name="Commande"
        verbose_name_plural="Commandes"

    def __str__(self):
        return self.contact.name


    
class Contact(models.Model):
    email=models.EmailField(max_length=200,verbose_name="Email",default=0)
    name=models.CharField(max_length=200,verbose_name="Nom",default=0)
    city=models.CharField(max_length=200,verbose_name="Ville",default=0)
    quarter=models.CharField(max_length=200,verbose_name="Quartier",default=0)
    street=models.CharField(max_length=200,verbose_name="Numéro de rue",default=0)
    door=models.CharField(max_length=200,verbose_name="Numéro de porte",default=0)
    phone=models.CharField(max_length=200,verbose_name="Téléphone",default=0)

    class Meta:
        verbose_name="Contact"
        verbose_name_plural="Contacts"
        
    def __str__(self):
        return self.name

        
        




                                
    
    
    
    
    


