from random import randint


from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from simple_search import search_filter

from Home.models import *
from Productos.models import *
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages




def DistribuidoresPaginado(request,distribuidores,cantidad):
    paginator = Paginator(distribuidores, cantidad)
    page = request.GET.get('page')
    return paginator.get_page(page)

def index(request):

    if not request.session.get('pedido'):
        request.session['pedido']=[]
        request.session.save()
        marca=Marca_Xurimotos.objects.last()
        request.session["logo"]= "/media/"+str(marca.logo)
        request.session["favicon"]="/media/"+str(marca.favicon)
        request.session["logo_pie_pag"] = "/media/" + str(marca.logo_pie_pag)
        request.session["whatsapp"] = marca.whatsapp
        request.session["telefono"] =   marca.telefono
        request.session["celular"] = marca.celular
        request.session["correo"] =   marca.correo
        request.session["direccion"] =   marca.direccion
        request.session["horario_lu_vier"] =   marca.horario_lu_vier
        request.session["horario_sab"] =   marca.horario_sab
        request.session["horario_dom"] =  marca.horario_dom
        request.session["facebook"] =   marca.facebook
        request.session["instagram"] =  marca.instagram
        request.session["tiktok"] = marca.tiktok
        request.session["youtube"] =  marca.youtube

    productos=Catalogo.objects.all().order_by('-id')[0:20]
    contexto ={
        'slider_fondo': Slider_fondo.objects.all().first(),
        'slider': Slider.objects.all(),
        'producto_carrusel': Producto_carrusel.objects.first(),
        'catalogo': productos,
        'blog': Blogs.objects.all(),
        'categorias':Categoria.objects.all().order_by('nombre'),
        'marcas':Marcas.objects.all().order_by('nombre'),
        'editable': Editable_Xurimotos.objects.all().first(),
        'destacado': Destacados_Xurimotos.objects.all().first(),
    }
    if request.POST:
        email = Suscripcion_Email.objects.create(email=request.POST['email'])
        email.save()
        messages.add_message(request, messages.SUCCESS, "Gracias por preferirnos!. Nuestro asesor se contactará contigo.")
    return render(request, 'new/index-corporate-7.html', contexto)

def empresa(request):
    contexto={
        'marca' : Marca_Xurimotos.objects.first(),
        'editable': Editable_Xurimotos.objects.all().first(),
        'destacado': Destacados_Xurimotos.objects.all().first(),
    }
    return render(request, 'new/about.html', contexto)



def prueba(request):
    contexto={
        'slider': Slider.objects.all(),

    }
    return render(request, 'new/prueba.html', contexto)


def blog(request):
    contexto={
        'marca': Marca_Xurimotos.objects.first(),
        'editable': Editable_Xurimotos.objects.all().first(),
        'destacado': Destacados_Xurimotos.objects.all().first(),

    }
    return render(request, 'new/about.html', contexto)


def post(request, n):

    contexto = {
        'editable': Editable_Xurimotos.objects.all().first(),
        'blogg': Blogs.objects.get(id=n),
        'blogs': Blogs.objects.all(),
    }
    return render(request, "new/blog-single.html", contexto)

def ubicacion_view(request):
    search_fields = ['lugar', 'local','direccion']
    ubica = Distribuidores_Xurimotos.objects.all().order_by('lugar')
    if request.GET.get('q'):
        ubica = ubica.filter(search_filter(search_fields, request.GET.get('q')))

    if request.GET.get('lugar'):
        ubica = ubica.filter(search_filter(search_fields, request.GET.get('lugar')))

    if request.GET.get('local'):
        ubica = ubica.filter(search_filter(search_fields, request.GET.get('local')))

    if request.GET.get('direccion'):
        ubica = ubica.filter(search_filter(search_fields, request.GET.get('direccion')))

    cantidad = ubica.count()

    por_pagina=20
    if request.GET.get('ppagina'):
        por_pagina=int(request.GET.get('ppagina'))

    ubicacion = Distribuidores_Xurimotos.objects.all().order_by('-id')[0:20]

    contexto={
        'marca' : Marca_Xurimotos.objects.first(),
        'editable': Editable_Xurimotos.objects.all().first(),
        'destacado': Destacados_Xurimotos.objects.all().first(),
        'ubicacion': DistribuidoresPaginado(request,ubica,por_pagina),
        'cantidad': cantidad,
        'distribuidores': ubicacion,


    }
    return render(request, 'new/ubicacion.html', contexto)

def contacto(request):
    # success = ""
    if request.method == "POST":
        subject = request.POST['subject']
        email = request.POST['email']
        celular = request.POST['celular']
        message = request.POST['message']

        template = render_to_string('new/email_template.html',{
            'subject': subject,
            'email': email,
            'celular': celular,
            'message': message,

        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['girekpruebas@gmail.com']
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'Se ha enviado tu correo.' )


    contexto={
        # 'messages': success,
        'marca': Marca_Xurimotos.objects.all().first(),
        'editable': Editable_Xurimotos.objects.all().first(),
        'destacado': Destacados_Xurimotos.objects.all().first(),
    }
    return render(request, 'new/contacto.html', contexto)

def distribuidores_view(request):
    search_fields = ['descripcion','categoria__nombre']
    prod = Distribuidores_Xurimotos.objects.all().order_by('lugar')
    if request.GET.get('q'):
        prod =prod.filter(search_filter(search_fields, request.GET.get('q')))

    if request.GET.get('lugar'):
        prod = prod.filter(search_filter(search_fields, request.GET.get('lugar')))

    if request.GET.get('local'):
       prod = prod.filter(search_filter(search_fields, request.GET.get('local')))

    if request.GET.get('direccion'):
       prod = prod.filter(search_filter(search_fields, request.GET.get('direccion')))

    cantidad=prod.count()

    por_pagina=20
    if request.GET.get('ppagina'):
        por_pagina=int(request.GET.get('ppagina'))


    contexto={
        'editable': Editable_Xurimotos.objects.all().first(),
        'marca_xurimotos': Marca_Xurimotos.objects.all().first(),
        'xpub': Market.objects.all(),
        'distribuidores':DistribuidoresPaginado(request,prod,por_pagina),
        'cantidad':cantidad,
        'categorias':Categoria.objects.all().order_by('nombre'),
        'galeria': Galeria.objects.all(),
        'marcas':Marcas.objects.all().order_by('nombre'),
        'destacado': Destacados_Xurimotos.objects.all().first(),

    }
    if request.GET.get('modo')=='Lista':
        return render(request, 'new/catalogo-lista.html', contexto)
    return render(request, 'new/distribuidores.html',contexto)

def arreglarProblemas(request):
    productos = Catalogo.objects.filter(categoria=None)
    for prod in productos:
        if not prod.categoria:
            cat = Categoria.objects.get(nombre=prod.aux)
            prod.categoria = cat
            prod.save()
    productos = Catalogo.objects.filter(color="SIN COLOR")
    for prod in productos:
        if prod.color == "SIN COLOR":
            prod.color = ""
            prod.save()
    return HttpResponse("Se aplicaron los cambios..!")

# def FormularioSuscripcion_Email(request):
#
#     if request.POST:
#         print(request.POST)
#         suscripcion = Suscripcion_Email.objects.create(email=request.POST['email'])
#         messages.add_message(request, messages.SUCCESS, "Gracias por preferirnos!. Nuestro asesor se contactará contigo.")
#         return HttpResponseRedirect("/")
#
#     else:
#         return HttpResponseRedirect("/")
#
