from colorfield.fields import ColorField
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe




class Marca_Xurimotos(models.Model):
    favicon = models.ImageField(upload_to='marca', null=True, blank=True, help_text='50x50 Icono de marca')
    logo = models.ImageField(upload_to='marca', null=True, blank=True , help_text='Logotipo de  marca')
    logo_pie_pag = models.ImageField(upload_to='marca', null=True, blank=True, help_text='Logotipo pie de  página marca')
    whatsapp = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Principal de WhatsApp')
    telefono = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Teléfono')
    celular = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Celular')
    telef_atencion_1 = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Teléfono Atención al cliente')
    telef_atencion_2 = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Teléfono Atención al cliente')
    celular_atencion_1  = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Celular Atención al cliente')
    celular_atencion_2  = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Celular Atención al cliente')
    telef_ventas_1  = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Teléfono Ventas')
    telef_ventas_2  = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Teléfono Ventas')
    celular_ventas_1  = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Celular Ventas')
    celular_ventas_2  = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Celular Ventas')
    telef_despacho_1  = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Teléfono Despacho')
    telef_despacho_2  = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Teléfono Despacho')
    celular_despacho_1 = models.CharField(max_length=15, null=True, blank=True,help_text='Contacto - Número Celular Despacho')
    celular_despacho_2  = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Celular Despacho')
    celular_soporte_tec_1  = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Celular Soporte Técnico')
    celular_soporte_tec_2  = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Celular Soporte Técnico')
    celular_marketing_ventas_1 = models.CharField(max_length=15, null=True, blank=True,help_text='Contacto - Número Celular Marketing & Ventas')
    celular_marketing_ventas_2  = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Celular Marketing & Ventas')
    celular_centro_ayuda_1  = models.CharField(max_length=15, null=True, blank=True, help_text='Contacto - Número Celular Centro de Ayuda')
    celular_centro_ayuda_2 = models.CharField(max_length=15, null=True, blank=True,help_text='Contacto - Número Celular Centro de Ayuda')
    correo = models.EmailField(null=True, blank=True, help_text='Contacto - Correo electrónico de empresa')
    direccion = models.CharField(max_length=100, null=True, blank=True, help_text='Contacto - Dirección de empresa')
    mapa= models.TextField(  null=True, blank=True, help_text='Link de Mapa Xuri Moto')
    horario_lu_vier = models.CharField(max_length=100, null=True, blank=True, help_text='Contacto - Horario de Lunes a Viernes empresa')
    horario_sab = models.CharField(max_length=100, null=True, blank=True, help_text='Contacto - Horario  Sabado empresa')
    horario_dom = models.CharField(max_length=100, null=True, blank=True, help_text='Contacto - Horario  Domingo empresa')
    facebook = models.CharField(max_length=100, null=True, blank=True, help_text='Redes Sociales - Facebook - Copiar y pegar  la dirección web de la empresa sin https://www.facebook.com/ ')
    instagram = models.CharField(max_length=100, null=True, blank=True, help_text='Redes Sociales - Instagram - Copiar y pegar  la dirección web de la empresa sin https://www.instagram.com/ ')
    tiktok = models.CharField(max_length=100, null=True, blank=True, help_text='Redes Sociales - Tiktok - Copiar y pegar  la dirección web de la empresa sin https://www.tiktok.com/ ')
    youtube = models.CharField(max_length=100, null=True, blank=True, help_text='Redes Sociales - Youtube - Copiar y pegar  la dirección web de la empresa sin https://www.youtube.com/ ')

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.logo)

    class Meta:
        verbose_name_plural = "1. Marca Xurimotos"


class Editable_Xurimotos(models.Model):
    slider_1_fondo = models.ImageField(upload_to='galeria', null=True, blank=True,  help_text='1680x617 - Secc-Inicio P1 Fondo Slider ')
    sub_1 = models.CharField(max_length=100, null=True, blank=True, help_text='Subtítulo 1 - Secc-Inicio P1')
    titulo_1 = models.CharField(max_length=100, null=True, blank=True, help_text='Título 1 - Secc-Inicio P1')
    detalle_1 = models.CharField(max_length=500, null=True, blank=True, help_text='Detalle 1 - Secc-Inicio P1')
    img_1_a = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='613x526 - Secc-Inicio P1 Slider Imagen 1')
    img_1_b = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='613x526 - Secc-Inicio P1 Slider Imagen 1')
    img_1_c = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='613x526 - Secc-Inicio P1 Slider Imagen 1')
    img_2 = models.ImageField(upload_to='galeria', null=True, blank=True,  help_text='613x526 - Secc-Inicio P2 Imagen 1')
    sub_2 = models.CharField(max_length=100, null=True, blank=True, help_text='Subtítulo 2 - Secc-Inicio P2 ')
    titulo_2 = models.CharField(max_length=100, null=True, blank=True, help_text='Título 2 - Secc-Inicio P2')
    detalle_2 = models.CharField(max_length=500, null=True, blank=True, help_text='Detalle 2 - Secc-Inicio P2')
    sub_3 = models.CharField(max_length=100, null=True, blank=True, help_text='Subtítulo 3 - Secc-Inicio P3')
    titulo_3 = models.CharField(max_length=100, null=True, blank=True, help_text='Título 3 - Secc-Inicio P3')
    detalle_3 = models.CharField(max_length=500, null=True, blank=True, help_text='Detalle 3 - Secc-Inicio P3')
    video = models.FileField(upload_to='galeria', null=True, blank=True, help_text='Video- Secc-Inicio p3 Video')
    img_fondo_vide_horiz = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='1920x420 - Secc-Inicio P3 Imagen Fondo Horizontal  Video')
    img_fondo_vide_verti = models.ImageField(upload_to='galeria', null=True, blank=True,help_text='1920x420 - Secc-Inicio P3 Imagen Fondo Vertical  Video')
    banner_img = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='1350x390 - Secc-Producto P3')
    mision_img_1 = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='660x840 - Secc-Empresa P1 Imagen misión')
    mision_img_2 = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='660x840 - Secc-Empresa P1 Imagen misión')
    mision_sub= models.CharField(max_length=100, null=True, blank=True, help_text='Subtítulo 1 - Secc-Empresa P1')
    mision_titulo = models.CharField(max_length=100, null=True, blank=True, help_text='Título 1 - Secc-Empresa P1')
    mision_detalle = models.CharField(max_length=500, null=True, blank=True, help_text='Detalle 1 - Secc-Empresa P1')
    vision_img_1 = models.ImageField(upload_to='galeria', null=True, blank=True,help_text='455x310- Secc-Empresa P1 Imagen misión')
    vision_img_2 = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='455x310 - Secc-Empresa P1 Imagen misión')
    vision_img_izq = models.ImageField(upload_to='galeria', null=True, blank=True,help_text='250x350 - Secc-Empresa P1 Imagen izquierda misión')
    vision_img_dere = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='350x250 - Secc-Empresa P1 Imagen  derecha misión')
    vision_sub = models.CharField(max_length=100, null=True, blank=True, help_text='Subtítulo 1 - Secc-Empresa P1')
    vision_titulo = models.CharField(max_length=100, null=True, blank=True, help_text='Título 1 - Secc-Empresa P1')
    vision_detalle = models.CharField(max_length=500, null=True, blank=True, help_text='Detalle 1 - Secc-Empresa P1')


    class Meta:
        verbose_name_plural = "2. Editable Xurimotos"

class Slider_fondo(models.Model):
    estado = models.BooleanField(default=False)
    tipo_archivo = models.CharField(max_length=20, default='imagen', choices=(("imagen", "imagen"), ("video", "video")))
    tipo_imagen = models.FileField(upload_to='slider', null=True, blank=True, help_text='imagen de 1280*500')
    tipo_video = models.FileField(upload_to='slider', null=True, blank=True, help_text='imagen de 1280*500')

    def miniatura(self):
        return mark_safe('<image width="300" height="150"  src="/media/%s">' % self.tipo_imagen)

    class Meta:
        verbose_name_plural = "3. Slider fondo Video"

class Slider(models.Model):
    estado = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='slider', null=True, blank=True, help_text='Inicio - Slider  Imagenes 500*900')

    # def delete(self, using=None, keep_parents=False):
    #     storage, path = self.imagen.storage, self.imagen.path
    #     super(Slider, self).delete()
    #     storage.delete(path)
    #
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     self.resize(self.imagen,500,300,'png')
    #     super(Slider, self).save()

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>" % self.imagen)

    class Meta:
        verbose_name_plural = "4. Slider Prodcutos"




class Destacados_Xurimotos(models.Model):
    dest_titulo_01 = models.CharField(max_length=100, null=True, blank=True, help_text='Título - Secc-Productos P3')
    dest_sub_titulo_01 = models.CharField(max_length=100, null=True, blank=True, help_text='Subtitulo - Secc-Productos P3')
    dest_titulo_02 = models.CharField(max_length=100, null=True, blank=True, help_text='Título - Secc-Productos P3')
    dest_link_02 = models.CharField(max_length=100, null=True, blank=True, help_text='Link  - Secc-Productos P3')
    dest_imagen_02 = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='325x275 - Secc-Productos P3 Imagen')
    dest_titulo_03 = models.CharField(max_length=100, null=True, blank=True, help_text='Título - Secc-Productos P3')
    dest_link_03 = models.CharField(max_length=100, null=True, blank=True, help_text='Link  - Secc-Productos P3')
    dest_imagen_03 = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='325x275 - Secc-Productos P3 Imagen')
    dest_titulo_04 = models.CharField(max_length=100, null=True, blank=True, help_text='Título - Secc-Productos P3')
    dest_link_04 = models.CharField(max_length=100, null=True, blank=True, help_text='Link  - Secc-Productos P3')
    dest_imagen_04 = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='325x275 - Secc-Productos P3 Imagen')
    dest_titulo_05 = models.CharField(max_length=100, null=True, blank=True, help_text='Título - Secc-Productos P3')
    dest_link_05 = models.CharField(max_length=100, null=True, blank=True, help_text='Link  - Secc-Productos P3')
    dest_imagen_05 = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='325x275 - Secc-Productos P3 Imagen')
    dest_titulo_06 = models.CharField(max_length=100, null=True, blank=True, help_text='Título - Secc-Productos P3')
    dest_link_06 = models.CharField(max_length=100, null=True, blank=True, help_text='Link  - Secc-Productos P3')
    dest_imagen_06 = models.ImageField(upload_to='galeria', null=True, blank=True,help_text='325x275 - Secc-Productos P3 Imagen')
    dest_titulo_07 = models.CharField(max_length=100, null=True, blank=True, help_text='Título - Secc-Productos P3')
    dest_link_07 = models.CharField(max_length=100, null=True, blank=True, help_text='Link  - Secc-Productos P3')
    dest_imagen_07 = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='325x275 - Secc-Productos P3 Imagen')
    dest_titulo_08 = models.CharField(max_length=100, null=True, blank=True, help_text='Título - Secc-Productos P3')
    dest_link_08 = models.CharField(max_length=100, null=True, blank=True, help_text='Link  - Secc-Productos P3')
    dest_imagen_08 = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='325x275 - Secc-Productos P3 Imagen')
    dest_titulo_09 = models.CharField(max_length=100, null=True, blank=True, help_text='Título - Secc-Productos P3')
    dest_link_09 = models.CharField(max_length=100, null=True, blank=True, help_text='Link  - Secc-Productos P3')
    dest_imagen_09 = models.ImageField(upload_to='galeria', null=True, blank=True,help_text='325x275 - Secc-Productos P3 Imagen')
    dest_titulo_10 = models.CharField(max_length=100, null=True, blank=True, help_text='Título - Secc-Productos P3')
    dest_link_10 = models.CharField(max_length=100, null=True, blank=True, help_text='Link  - Secc-Productos P3')
    dest_imagen_10 = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='325x275 - Secc-Productos P3 Imagen')


    class Meta:
        verbose_name_plural = "5. Destacados Xurimotos"




class Producto_carrusel(models.Model):
    estado = models.BooleanField(default=False)
    titulo = models.CharField(max_length=100, null=True, blank=True, help_text='Título - Secc-Productos')
    enlace = models.CharField(max_length=100, null=True, blank=True, help_text='Link - Secc-Productos ')
    imagen_1 = models.ImageField(upload_to='carrusel', null=True, blank=True, help_text='368X313 Producto - Carrusel')
    codigo_color_imag_1 = ColorField(default="#FFFFFF")
    imagen_2 = models.ImageField(upload_to='carrusel', null=True, blank=True, help_text='368X313 Producto - Carrusel')
    codigo_color_imag_2 = ColorField(default="#FFFFFF")
    imagen_3 = models.ImageField(upload_to='carrusel', null=True, blank=True, help_text='368X313 Producto - Carrusel')
    codigo_color_imag_3 = ColorField(default="#FFFFFF")
    imagen_4 = models.ImageField(upload_to='carrusel', null=True, blank=True, help_text='368X313 Producto - Carrusel')
    codigo_color_imag_4 = ColorField(default="#FFFFFF")
    imagen_5 = models.ImageField(upload_to='carrusel', null=True, blank=True, help_text='368X313 Producto - Carrusel')
    codigo_color_imag_5 = ColorField(default="#FFFFFF")

    def __str__(self):
        return self.titulo

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>" % self.imagen_1)

    class Meta:
        verbose_name_plural = "6. Producto Carrusel"





class Distribuidores_Xurimotos(models.Model):
    lugar = models.CharField(max_length=100, null=True, blank=True, help_text='Ingresar ubicación del local')
    local = models.CharField(max_length=100, null=True, blank=True, help_text='Ingresar nombre del local')
    direccion = models.CharField(max_length=150, null=True, blank=True, help_text='Ingresar dirección del local')
    correo= models.EmailField( null=True, blank=True, help_text='Ingresar correo de local')
    horario = models.CharField(max_length=500, null=True, blank=True, help_text='Ingresar horario de atención del local')
    imagen = models.ImageField(upload_to='galeria', null=True, blank=True, help_text='410x300 Ingresar foto del local')
    contacto= models.CharField(max_length=150, null=True, blank=True, help_text='Ingresar contacto del local')
    ubicacion = models.CharField(max_length=700, null=True, blank=True, help_text='Ingresar contacto del local')

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>"%self.imagen)

    class Meta:
        verbose_name_plural = "8. Distribuidores Xurimotos"

# class Market(models.Model):
#     titulo = models.CharField(max_length=100, null=True, blank=True)
#     imagen = models.ImageField(upload_to='market', null=True, blank=True, help_text='Imagenes de la Comunidad de Xurimoto')
#
#     def miniatura(self):
#         return mark_safe("<img src='/media/%s' style='width: 200px'>"%self.imagen)
#
#     class Meta:
#         verbose_name_plural = "8. Publicidad "


class Blogs(models.Model):
    tipo_archivo = models.CharField(max_length=20, default='imagen', choices=(("imagen", "imagen"), ("video", "video")))
    tipo_imagen = models.FileField(upload_to='blog', null=True, blank=True, help_text='imagen de 1280*500')
    tipo_video_link = models.CharField(max_length=120, null=True, blank=True)
    fecha=models.DateField()
    titulo=models.CharField(max_length=200, null=True, blank=True)
    articulo=models.TextField(max_length=10000, null=True, blank=True)
    autor = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):

        return '%s ' % (self.titulo)


    def miniatura(self):
        return mark_safe('<image width="300" height="150"  src="/media/%s">' % self.tipo_imagen)

    class Meta:
        verbose_name_plural = "9. Blogs"


class Suscripcion_Email(models.Model):
    email=models.EmailField(max_length=200)

    class Meta:
        verbose_name_plural = "9.1. Suscripción Email"


class Envio_Email(models.Model):
    servidor_smtp=models.CharField(max_length=100)
    puerto=models.IntegerField()
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=100)
    copia=models.EmailField(max_length=200)
    mensaje_personalizado = models.TextField(default="Gracias por elegir xurimotos")



