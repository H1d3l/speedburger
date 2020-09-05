from django.db import models

# Create your models here.


class Hamburguer(models.Model):
    TYPE_BREAD_CHOICE = [
        ('PAO1',"PAO1"),
        ('PAO2',"PAO2"),
        ('PAO3',"PAO3"),
        ('PAO4',"PAO4"),
    ]
    name = models.CharField(max_length = 50)
    description = models.TextField()
    value = models.FloatField()
    type_bread = models.CharField(max_length = 10,choices = TYPE_BREAD_CHOICE,default='PAO1')


    class Meta:
        ordering = ['value']

    def __str__(self):
        return self.name





class ComboHamburguer(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    value = models.FloatField()
    
    
    class Meta:
        ordering = ['value']

    def __str__(self):
        return self.name