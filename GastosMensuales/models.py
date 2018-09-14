# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    
    def __str__(self):
        return 'Categoria {}'.format(self.id, self.nombre)
    
    
    
class Gasto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name="Categorias", on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    
    def suma(self):
        total=0.0
        for producto in self.productos.all():
            total += producto.precio
        return total
        
          
    def __str__(self):
        return "{}".format(self.id, self.categoria)
    
class Producto(models.Model):
    gasto = models.ForeignKey(Gasto, related_name="productos")
    nombreP = models.CharField('nombreP', max_length=50)
    precio = models.FloatField()
    
    
    def __str__(self):
        return 'Producto {}'.format(self.gasto, self.nombreP, self.precio)
