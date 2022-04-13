from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Font
from simple_search import search_filter
from Home.models import Marca_Xurimotos, Editable_Xurimotos, Destacados_Xurimotos, Producto_carrusel
from Productos.models import Catalogo, Categoria, Marcas, Pedidos, DetallePedido, Galeria
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
    search_fields = ['descripcion','categoria__nombre']
    prod = Catalogo.objects.all().order_by('descripcion')
    if request.GET.get('q'):
        prod =prod.filter(search_filter(search_fields, request.GET.get('q')))

    if request.GET.get('color'):
        prod = prod.filter(search_filter(search_fields, request.GET.get('color')))

    if request.GET.get('cat'):
       prod = prod.filter(search_filter(search_fields, request.GET.get('cat')))

    if request.GET.get('marca'):
       prod = prod.filter(search_filter(search_fields, request.GET.get('marca')))

    if request.GET.get('edades'):
        if request.GET.get("edades")=="a":
            prod = prod
        else:
            prod = prod.filter(search_filter(search_fields, request.GET.get('edades')))
    cantidad=prod.count()

    por_pagina=20
    if request.GET.get('ppagina'):
        por_pagina=int(request.GET.get('ppagina'))

    productos = Catalogo.objects.all().order_by('-id')[0:20]
    contexto={
        'marca_xurimotos': Marca_Xurimotos.objects.all().first(),
        'productos':CatalogoPaginado(request,prod,por_pagina),
        'cantidad':cantidad,
        'catalogo': productos,
        'producto_carrusel': Producto_carrusel.objects.first(),
        'categorias':Categoria.objects.all().order_by('nombre'),
        'galeria': Galeria.objects.all(),
        'marcas':Marcas.objects.all().order_by('nombre'),
        'colores':getColores(prod),
        'editable': Editable_Xurimotos.objects.all().first(),
        'destacado': Destacados_Xurimotos.objects.all().first(),

    }
    if request.GET.get('modo')=='Lista':
        return render(request, 'new/catalogo-lista.html', contexto)
    return render(request, 'new/productos.html',contexto)



def catalogo_view(request):
    search_fields = ['descripcion','categoria__nombre']
    prod = Catalogo.objects.all().order_by('descripcion')
    if request.GET.get('q'):
        prod =prod.filter(search_filter(search_fields, request.GET.get('q')))

    if request.GET.get('color'):
        prod = prod.filter(search_filter(search_fields, request.GET.get('color')))

    if request.GET.get('cat'):
       prod = prod.filter(search_filter(search_fields, request.GET.get('cat')))

    if request.GET.get('marca'):
       prod = prod.filter(search_filter(search_fields, request.GET.get('marca')))

    if request.GET.get('edades'):
        if request.GET.get("edades")=="a":
            prod = prod
        else:
            prod = prod.filter(search_filter(search_fields, request.GET.get('edades')))
    cantidad=prod.count()

    por_pagina=20
    if request.GET.get('ppagina'):
        por_pagina=int(request.GET.get('ppagina'))

    productos = Catalogo.objects.all().order_by('-id')[0:20]
    contexto={
        'marca_xurimotos': Marca_Xurimotos.objects.all().first(),
        'catalogo': productos,
        'productos':CatalogoPaginado(request,prod,por_pagina),
        'cantidad':cantidad,
        'categorias':Categoria.objects.all().order_by('nombre'),
        'galeria': Galeria.objects.all(),
        'marcas':Marcas.objects.all().order_by('nombre'),
        'colores':getColores(prod),
        'editable': Editable_Xurimotos.objects.all().first(),
        'destacado': Destacados_Xurimotos.objects.all().first(),

    }
    if request.GET.get('modo')=='Lista':
        return render(request, 'new/catalogo-lista.html', contexto)
    return render(request, 'new/catalogo.html',contexto)





def detalles_producto(request):
    todos=Catalogo.objects.all()
    prod=todos.get(id=request.GET.get('id'))
    pr=prod.descripcion.split()
    contexto={
        'editable': Editable_Xurimotos.objects.all().first(),
        'marca_xurimotos': Marca_Xurimotos.objects.all().first(),
        'producto':prod,
        'relacionados':todos.filter(descripcion__icontains=pr[0]+ " "+ pr[1]).order_by('-id')
    }
    return render(request, 'new/product.html', contexto)

def addPedido(request):
    producto=Catalogo.objects.get(id=request.GET.get("id"))
    res=False
    for x in request.session["pedido"]:
        print('ya esta')
        if x[0]==producto.id:
            res=True
    if res==False:
        request.session["pedido"].append([producto.id,{"cantidad":request.GET.get("x"),"foto":str(producto.foto),"nombre":producto.descripcion}])
        request.session.save()
        print(request.session["pedido"])
        return HttpResponse('ok')
    else:
        return HttpResponse('no')

def eliminarItemPedido(request):
    lista=[]
    uri=request.GET.get('uri')
    for producto in request.session['pedido']:
        id, p= producto
        if not int(id)==int(request.GET.get('id')):
            lista.append(producto)
    request.session['pedido']=lista
    request.session.save()
    return HttpResponseRedirect(uri)

def editarCantidadItem(request):
    lista=[]
    for producto in request.session['pedido']:
        id, p= producto
        if int(id)==int(request.GET.get('id')):
            p['cantidad']=int(request.GET.get('cantidad'))
            lista.append([id,p])
        else:
            lista.append(producto)
    request.session['pedido']=lista
    request.session.save()
    return HttpResponse("ok")


def vaciarPedido(request):
    if request.session.get('pedido'):
        request.session['pedido']=[]
        request.session.save()
    return HttpResponseRedirect("/")


def verPedido(request):
    cuantos=len(request.session['pedido'])
    contexto={
        'cuantos':cuantos,
        'productos':Catalogo.objects.all().order_by('descripcion')[0:50]
    }
    return render(request, "new/shop-cart.html",contexto)

def obtenerPedido(request, id):
    request.session['pedido']=[]
    request.session.save()
    contexto = {
        'pedido': Pedidos.objects.get(id=id)
    }
    return render(request, 'new/shop-order-complete.html', contexto)


def crearExcel(request,id):
    pedido=Pedidos.objects.get(id=id)
    ruta = os.path.join(BASE_DIR, 'static/xurimotos.png')
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename={date}-movies.xlsx'.format(
        date=datetime.datetime.now().strftime('%Y-%m-%d'),
    )
    wb = Workbook()
    hoja = wb.active
    ft = Font(color="c1760c",bold=True)
    img = Image(ruta)
    hoja.add_image(img, 'A1')
    hoja.append(())
    hoja.append(())
    hoja.append(())
    hoja.append(())
    hoja.append(('Orden No.',str.zfill(str(pedido.id),10)))
    hoja.append(('Fecha:', str(pedido.fecha.date())))
    hoja.append(('Nombre del Cliente:', pedido.nombre))
    hoja.append(('Cédula: ', pedido.cedula))
    hoja.append(('Dirección:', pedido.direccion+" - "+pedido.ciudad))
    hoja.merge_cells('B9:D9')
    hoja.append(('Telefono:', pedido.telefono, pedido.email))
    hoja.append(('Ciudad: ', pedido.ciudad))
    hoja.append(())
    hoja.merge_cells('A13:D13')
    hoja.append(('ID', 'CÓDIGO', 'DESCRIPCIÓN', 'CANTIDAD'))
    a1 = hoja['A14']
    b1 = hoja['B14']
    c1 = hoja['C14']
    d1 = hoja['D14']
    a1.font=ft
    b1.font = ft
    c1.font = ft
    d1.font = ft
    hoja.column_dimensions['A'].width = 20
    hoja.column_dimensions['B'].width = 20
    hoja.column_dimensions['C'].width = 100
    hoja.column_dimensions['D'].width = 20
    path=os.path.join(BASE_DIR,'media/excel/')
    filename=path+'pedido-%s.xlsx'%str.zfill(str(id),10)
    for producto in pedido.detallepedido_set.all():
        hoja.append((producto.producto_id,producto.producto.codigo,producto.producto.descripcion,producto.cantidad))
    wb.save(response)
    wb.save(filename)
    enviar_email_adjunto([pedido.email,],"Mensaje de la Aplicación - Solicitud de pedido",filename,'pedido-%s.xlsx'%str.zfill(str(id),10))
    #return response


def registrarPedido(request):
    if request.POST:
        pedido=Pedidos.objects.create(
            cedula=request.POST.get('cedula'),
            nombre=request.POST.get('nombre'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono'),
            ciudad=request.POST.get('ciudad'),
            direccion=request.POST.get('direccion'))
        pedido.save()
        for producto in request.session['pedido']:
            id, p= producto
            cantidad =0
            if p['cantidad']==None:
                cantidad=1
            else:
                cantidad=p['cantidad']
            DetallePedido.objects.create(
                pedido=pedido,
                producto_id=id,
                cantidad=cantidad
            ).save()
        crearExcel(request, pedido.id)
        return HttpResponseRedirect("/getPedido/%s"%pedido.id)
