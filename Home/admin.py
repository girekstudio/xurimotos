from django.contrib import admin

# Register your models here.
from Home.models import *
from xurimotos.snippers import Attr



@admin.register(Marca_Xurimotos)
class Marca_XurimotosAdmin(admin.ModelAdmin):
    list_display = Attr(Marca_Xurimotos) + ["miniatura"]
    list_display_links = Attr(Marca_Xurimotos)

@admin.register(Editable_Xurimotos)
class Editable_XurimotosAdmin(admin.ModelAdmin):
    list_display = Attr(Editable_Xurimotos)
    list_display_links = Attr(Editable_Xurimotos)

@admin.register(Distribuidores_Xurimotos)
class Distribuidores_XurimotosAdmin(admin.ModelAdmin):
    list_display = Attr(Distribuidores_Xurimotos) + ["miniatura"]
    list_display_links = Attr(Distribuidores_Xurimotos)

@admin.register(Destacados_Xurimotos)
class Destacados_XurimotosAdmin(admin.ModelAdmin):
    list_display = Attr(Destacados_Xurimotos)
    list_display_links = Attr(Destacados_Xurimotos)

@admin.register(Menu_Destacados_Xurimotos)
class Menu_Destacados_XurimotosAdmin(admin.ModelAdmin):
    list_display = Attr(Menu_Destacados_Xurimotos)
    list_display_links = Attr(Menu_Destacados_Xurimotos)

@admin.register(Producto_carrusel)
class Producto_carruselAdmin(admin.ModelAdmin):
    list_display = Attr(Producto_carrusel)
    list_display_links = Attr(Producto_carrusel)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = Attr(Slider)+["miniatura"]
    list_display_links = Attr(Slider)

@admin.register(Slider_fondo)
class Slider_fondoAdmin(admin.ModelAdmin):
    list_display = Attr(Slider_fondo)+["miniatura"]
    list_display_links = Attr(Slider_fondo)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = Attr(Banner)+["miniatura"]
    list_display_links = Attr(Banner)


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = Attr(Blogs)+["miniatura"]
    list_display_links = Attr(Blogs)

@admin.register(Suscripcion_Email)
class modelo(admin.ModelAdmin):
    list_display = Attr(Suscripcion_Email)
    list_display_links = Attr(Suscripcion_Email)


