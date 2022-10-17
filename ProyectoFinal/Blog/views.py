from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import Autor, Articulo, Section
#para login,logout,register
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#para list y detalles, etc (clase 22)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse



# Create your views here.
@login_required
def mostrar_inicio(request):    
    return render(request,"Blog/inicio.html")

def mostrar_autores(request):
    return render(request,"Blog/autor.html")


def mostrar_articulos(request):
    return render(request,"Blog/articulo.html")


def mostrar_seccion(request):
    return render(request,"Blog/seccion.html")


def procesar_formulario_autor(request):
    if request.method !="POST":
        return render(request, "Blog/formulario_autor.html")
    
    autor=Autor ( nombre=request.POST["nombre"],apellido=request.POST["apellido"],profesion=request.POST["profesion"])
    autor.save()
    return render(request,"Blog/inicio.html")

def procesar_formulario_articulo(request):
    if request.method !="POST":
        return render(request, "Blog/formulario_articulo.html")
    
    articulo=Articulo ( titulo=request.POST["titulo"],fecha=request.POST["fecha"],texto=request.POST["texto"])
    articulo.save()
    return render(request,"Blog/inicio.html")

def procesar_formulario_seccion(request):
    if request.method !="POST":
        return render(request, "Blog/formulario_seccion.html")
    
    seccion=Section ( nombre=request.POST["nombre"])
    seccion.save()
    return render(request,"Blog/inicio.html")

def busqueda(request):
    return render(request, "Blog/busqueda.html")

def buscar (request):

    if not request.GET["apellido"]:
        return HttpResponse ("No se enviaron datos")
    else: 
        apellido_buscado= request.GET["apellido"]
        autores = Autor.objects.filter(apellido = apellido_buscado)
                
        contexto={
            "apellido": apellido_buscado,
             "autores": autores
             }
    
    return render(request, "Blog/resultado_busqueda.html", contexto)


#LOGIN, LOGOUT; REGISTER

class MyLogin(LoginView):
    template_name="Blog/login.html"


class MyLogout(LogoutView, LoginRequiredMixin):
    template_name="Blog/logout.html"
    

def register(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            
            return render (request,"Blog/inicio.html",{"mensaje":f"Usuario: {username}"})
    
    form=UserCreationForm()
        
    return render(request,"Blog/register.html",{"form":form})    
