from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from Productos.models import Catalogo, Galeria, Categoria, Marcas, Pedidos, DetallePedido
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
    search_fields = ['codigo','descripcion',]
    inlines = [GaleriaInline]
    list_filter = ['categoria','color',]
    readonly_fields = ['precio_final',]

@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = Attr(Galeria)
    list_display_links = Attr(Galeria)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = Attr(Categoria)
    list_display_links = Attr(Categoria)

@admin.register(Marcas)
class MarcasAdmin(admin.ModelAdmin):
    list_display = Attr(Marcas)
    list_display_links = Attr(Marcas)

# class DetallePedidoInline(admin.StackedInline):
#     model = DetallePedido
#     extra = 0

# @admin.register(Pedidos)
# class PedidosAdmin(admin.ModelAdmin):
#     list_display = Attr(Pedidos)+["verPedido"]
#     list_display_links = Attr(Pedidos)
#     inlines = [DetallePedidoInline]

# @admin.register(DetallePedido)
# class DetallePedidoAdmin(admin.ModelAdmin):
#     list_display = Attr(DetallePedido)
#     list_display_links = Attr(DetallePedido)
