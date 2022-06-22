from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from Productos.models import Catalogo, Galeria, Categoria
from Productos.resource import CatalogoResource
from xurimotos.snippers import Attr

class GaleriaInline(admin.StackedInline):
    model = Galeria
    extra = 0

@admin.register(Catalogo)
class CatalogoAdmin(ImportExportModelAdmin):
    resource_class =CatalogoResource
    list_display = Attr(Catalogo)
    list_display_links = Attr(Catalogo)
    search_fields = ['codigo','nombre_producto',]
    inlines = [GaleriaInline]
    list_filter = ['categoria',]

@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = Attr(Galeria)
    list_display_links = Attr(Galeria)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = Attr(Categoria)
    list_display_links = Attr(Categoria)




