
from django.db import models
 
from accounts.models import User
# Create your models here.


class Categories(models.Model):
    name=models.CharField(max_length=100)
    
    # Standar
    statut = models.BooleanField(default=True)
    updated= models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Categories"
        ordering=['-updated', '-created']


class SousCategories(models.Model):
    name = models.CharField(max_length=100)
    categorie = models.ManyToManyField(Categories, related_name="sous_categories")
    # Standar
    statut = models.BooleanField(default=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = "Sous-Catégorie"
        verbose_name_plural = "Sous-Catégories"
        ordering=['-updated', '-created']
        
class Tags(models.Model):
    name=models.CharField(max_length=100)
    
    # Standar
    statut = models.BooleanField(default=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering=['-updated', '-created']

       
        
        
class Marques(models.Model):
    name=models.CharField(max_length=100)
    
    # Standar
    statut = models.BooleanField(default=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Marque"
        verbose_name_plural = "Marques"
        ordering=['-updated', '-created']
        
        
class Images(models.Model):
    name=models.CharField(max_length=155)
    imgP=models.FileField(upload_to="image_articles/%y")
    imgS=models.FileField(upload_to="image_articles/%y",null=True, blank=True)
    imgT=models.FileField(upload_to="image_articles/%y",null=True, blank=True)
    
    # Standar
    statut = models.BooleanField(default=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering=['-updated', '-created']
        
class Caracteristiques(models.Model):
    name = models.CharField(max_length=155)
    valeur = models.CharField(max_length=7)
   
    # Standar
    statut = models.BooleanField(default=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.valeur
    
    class Meta:
        verbose_name = "Caractéristique"
        verbose_name_plural = "Caractéristiques"
        ordering=['-updated', '-created']
        
class Products(models.Model):
    name=models.CharField(max_length=240)
    description=models.TextField(null=True, blank=True)
    seller=models.ForeignKey(User, on_delete=models.CASCADE)
    marque=models.ForeignKey(Marques, on_delete=models.CASCADE,related_name="all_products")
    sous_category=models.ForeignKey(SousCategories, on_delete=models.CASCADE, related_name="all_products")
    caracteristiques = models.ManyToManyField(Caracteristiques, blank=True )
    image=models.ForeignKey(Images, on_delete=models.CASCADE)
    price=models.FloatField(default=0.0)
    stock=models.IntegerField(default=0)
    
    
    # Standar
    statut = models.BooleanField(default=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering=['-updated', '-created']
        
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.product.name}({self.quantity})"
    
    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"
        

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    
    # Standar
    statut = models.BooleanField(default=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
    
    class Meta:
        verbose_name = "Panier"
        verbose_name_plural = "Panier"
        ordering=['-updated', '-created']

    