
import os
from django.db import models
# Create your models here.
from django.utils.safestring import mark_safe

from xurimotos.settings import BASE_DIR
from xurimotos.snippers import ResizeImageMixin

class Categoria(models.Model,ResizeImageMixin):
    nombre=models.CharField(max_length=50)
    icono=models.ImageField(upload_to="icono",null=True,blank=True)
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.icono:
            self.resize(imageField=self.icono, ancho=100, alto=100, format='png')
        super(Categoria, self).save()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural="1. Categorias"

class Catalogo(models.Model,ResizeImageMixin):
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True,blank=True)
    aux=models.CharField(null=True,blank=True,max_length=300)
    codigo=models.CharField(max_length=30)
    descripcion=models.TextField()
    info_tecnica = models.TextField(null=True,blank=True,max_length=900)
    unidad_medida =models.CharField(max_length=10)
    unidades_por_caja= models.CharField(max_length=50)
    precio_unitario =models.DecimalField(max_digits=9, decimal_places=2)
    descuento=models.IntegerField(default=30)
    foto= models.ImageField(null=True,blank=True,upload_to='producto')
    precio_final=models.DecimalField(max_digits=9, decimal_places=2,default=0)
    color=models.CharField(max_length=200,null=True,blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        cat=None
        try:
            cat =Categoria.objects.get(nombre=str.upper(self.aux))
        except:
            cat=Categoria.objects.create(nombre=str.upper(self.aux)).save()
        self.categoria=cat

        if self.color:
            self.color=str.upper(self.color)

        if not self.foto:
            self.foto='xuri.jpg'
        else:
            self.resize(imageField=self.foto, ancho=800, alto=800, format='png', marca=(300, 300))
        self.precio_final = float(self.precio_unitario) - float(self.precio_unitario) * (float(self.descuento)) / 100
        super(Catalogo, self).save()

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="3. Catalogo de Productos"

class Galeria(models.Model,ResizeImageMixin):
    producto=models.ForeignKey(Catalogo,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='producto/galeria')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        gale = None

        if not self.imagen:
            self.imagen = 'xuri.jpg'
        else:
            self.resize(imageField=self.imagen, ancho=800, alto=800, format='png', marca=(300, 300))
        super(Galeria, self).save()
    class Meta:
        verbose_name_plural="4. Galeria"

class Marcas(models.Model,ResizeImageMixin):
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='marcas',null=True,blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.imagen:
            self.resize(imageField=self.imagen,ancho=120,alto=80,format='png')
        super(Marcas, self).save()

    class Meta:
        verbose_name_plural="2. Marcas"

class Pedidos(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    cedula=models.CharField(max_length=13)
    nombre=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    telefono=models.CharField(max_length=13)
    ciudad=models.CharField(max_length=60)
    direccion=models.CharField(max_length=200)

    def verPedido(self):
        return mark_safe('<a taget="_blank" href="/media/excel/pedido-%s.xlsx">Ver el Pedido</a>'%str.zfill(str(self.id),10))

    class Meta:
        verbose_name_plural="4. Pedidos"

class DetallePedido(models.Model):
    pedido=models.ForeignKey(Pedidos,on_delete=models.CASCADE)
    producto=models.ForeignKey(Catalogo,on_delete=models.CASCADE)
    cantidad=models.IntegerField()
