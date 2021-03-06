
import os
from django.db import models
# Create your models here.
from django.utils.safestring import mark_safe

from xurimotos.settings import BASE_DIR
from xurimotos.snippers import ResizeImageMixin

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural="1. Categorias"

class Catalogo(models.Model,ResizeImageMixin):
    aux = models.CharField(null=True, blank=True, max_length=300)
    codigo = models.CharField(max_length=30, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    nombre_producto = models.TextField(null=True, blank=True, max_length=300)
    detalle = models.TextField()
    info_tecnica = models.TextField(null=True, blank=True, max_length=1000)
    foto = models.ImageField(null=True, blank=True, upload_to='producto')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        cat = None
        try:
            cat = Categoria.objects.get(nombre=str.upper(self.aux))
        except:
            cat = Categoria.objects.create(nombre=str.upper(self.aux)).save()
        self.categoria = cat

        if not self.foto:
            self.foto = 'xuri.jpg'
        else:
            self.resize(imageField=self.foto, ancho=800, alto=800, format='png' )
        super(Catalogo, self).save()

    def __str__(self):
        return self.nombre_producto

    class Meta:
        verbose_name_plural = "2. Catalogo de Productos"


class Galeria(models.Model,ResizeImageMixin):
    producto=models.ForeignKey(Catalogo,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='producto/galeria')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        gale = None

        if not self.imagen:
            self.imagen = 'xuri.jpg'
        else:
            self.resize(imageField=self.imagen, ancho=800, alto=800, format='png')
        super(Galeria, self).save()
    class Meta:
        verbose_name_plural="3. Galeria de Productos"




