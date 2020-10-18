from django.db import models

# Create your models here.


class Product(models.Model):
    TYPE_PRODUCT_CHOICE = [
        ('Hamburguer',"Hamburguer"),
        ('Batata Frita',"Batata Frita"),
        ('Pastel',"Pastel"),
        ('Bebidas',"Bebidas"),
        ('Adicionais',"Adicionais"),
    ]
    name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to="hamburguer/",default = 'default.png',blank=True) 
    description = models.TextField()
    price = models.DecimalField(default = 0,decimal_places=2, max_digits=8)
    type_product = models.CharField(max_length = 30,choices = TYPE_PRODUCT_CHOICE,default='Hamburguer')


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name





class Combo(models.Model):
    name = models.CharField(max_length = 50)
    image = models.ImageField(default = 'defalt.png',blank=True)
    description = models.TextField()
    price = models.DecimalField(default = 0,decimal_places=2, max_digits=8)


    
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name