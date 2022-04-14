from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Font
from simple_search import search_filter
from Home.models import Marca_Xurimotos, Editable_Xurimotos, Destacados_Xurimotos, Producto_carrusel
from Productos.models import Catalogo, Categoria, Marcas, Galeria
import os
import datetime
from xurimotos.settings import BASE_DIR



def CatalogoPaginado(request,catalogo,cantidad):
    paginator = Paginator(catalogo, cantidad)
    page = request.GET.get('page')
    return paginator.get_page(page)

def getColores(prod):
    lista=[]
    for p in prod:
        if p.color:
            lista+=str.upper(p.color).split(",")
    lista2=[]
    for x in lista:
        lista2.append(x.lstrip())
    lista2 = set(lista2)
    lista2 = sorted(lista2)
    return lista2


def producto_view(request):
    search_fields = ['nombre_producto','categoria__nombre']
    prod = Catalogo.objects.all().order_by('nombre_producto')
    if request.GET.get('q'):
        prod =prod.filter(search_filter(search_fields, request.GET.get('q')))

    # if request.GET.get('color'):
    #     prod = prod.filter(search_filter(search_fields, request.GET.get('color')))

    if request.GET.get('cat'):
       prod = prod.filter(search_filter(search_fields, request.GET.get('cat')))

    if request.GET.get('marca'):
       prod = prod.filter(search_filter(search_fields, request.GET.get('marca')))

    # if request.GET.get('edades'):
    #     if request.GET.get("edades")=="a":
    #         prod = prod
    #     else:
    #         prod = prod.filter(search_filter(search_fields, request.GET.get('edades')))
    # cantidad=prod.count()

    por_pagina=20
    if request.GET.get('ppagina'):
        por_pagina=int(request.GET.get('ppagina'))

    productos = Catalogo.objects.all().order_by('-id')[0:20]
    contexto={
        'marca_xurimotos': Marca_Xurimotos.objects.all().first(),
        'productos':CatalogoPaginado(request,prod,por_pagina),
        'catalogo': productos,
        'producto_carrusel': Producto_carrusel.objects.first(),
        'categorias':Categoria.objects.all().order_by('nombre'),
        'galeria': Galeria.objects.all(),
        'marcas':Marcas.objects.all().order_by('nombre'),
        # 'colores':getColores(prod),
        'editable': Editable_Xurimotos.objects.all().first(),
        'destacado': Destacados_Xurimotos.objects.all().first(),

    }
    if request.GET.get('modo')=='Lista':
        return render(request, 'new/catalogo-lista.html', contexto)
    return render(request, 'new/productos.html',contexto)



def catalogo_view(request):
    search_fields = ['nombre_producto','categoria__nombre']
    prod = Catalogo.objects.all().order_by('nombre_producto')
    if request.GET.get('q'):
        prod =prod.filter(search_filter(search_fields, request.GET.get('q')))

    if request.GET.get('cat'):
       prod = prod.filter(search_filter(search_fields, request.GET.get('cat')))

    if request.GET.get('marca'):
       prod = prod.filter(search_filter(search_fields, request.GET.get('marca')))

    por_pagina=20
    if request.GET.get('ppagina'):
        por_pagina=int(request.GET.get('ppagina'))

    productos = Catalogo.objects.all().order_by('-id')[0:20]
    contexto={
        'marca_xurimotos': Marca_Xurimotos.objects.all().first(),
        'catalogo': productos,
        'productos':CatalogoPaginado(request,prod,por_pagina),
        # 'cantidad':cantidad,
        'categorias':Categoria.objects.all().order_by('nombre'),
        'galeria': Galeria.objects.all(),
        'marcas':Marcas.objects.all().order_by('nombre'),
        # 'colores':getColores(prod),
        'editable': Editable_Xurimotos.objects.all().first(),
        'destacado': Destacados_Xurimotos.objects.all().first(),

    }
    if request.GET.get('modo')=='Lista':
        return render(request, 'new/catalogo-lista.html', contexto)
    return render(request, 'new/catalogo.html',contexto)


def detalles_producto(request):
    todos=Catalogo.objects.all()
    prod=todos.get(id=request.GET.get('id'))
    pr=prod.nombre_producto.split()
    contexto={
        'editable': Editable_Xurimotos.objects.all().first(),
        'marca_xurimotos': Marca_Xurimotos.objects.all().first(),
        'producto':prod,
        'relacionados':todos.filter(nombre_producto__icontains=pr[0]+ " "+ pr[1]).order_by('-id')
    }
    return render(request, 'new/product.html', contexto)
