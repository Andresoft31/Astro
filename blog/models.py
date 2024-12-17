from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category( models.Model):

    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add =True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de edicion")

    class Meta:

        verbose_name = " categoria"
        verbose_name_plural  = "categorias"
        ordering = ['-created']

    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):

    title= models.CharField(max_length=200)
    content= models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Entrada(models.Model):

    title= models.CharField(max_length=200 )
    subtitle = models.CharField( max_length =200, blank=True )
    descripcion =  models.TextField()
    fecha_creacion  = models.DateTimeField( auto_now_add= True)

    def __str__(self):

        return self.title

