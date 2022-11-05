from django.contrib import admin
from multiprocessing import context
from re import template
from django.urls import path
from django.urls import path 
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from Blog.views import (
        mostrar_inicio, mostrar_articulos, mostrar_autores, mostrar_seccion,
        busqueda, buscar, formulario_autor, 
        formulario_articulo, formulario_seccion,
        MyLogin, login_request, register, editar_perfil

      )


urlpatterns = [
    path('', mostrar_inicio),
    path("inicio/",mostrar_inicio, name="inicio"),
    path("autor/",mostrar_autores, name="autor"),
    path("articulo/",mostrar_articulos, name="articulo"),
    path("seccion/",mostrar_seccion, name="seccion"),
    path ("formulario_autor/", formulario_autor, name="formulario_autor"),
    path ("formulario_articulo/", formulario_articulo, name="formulario_articulo"),
    path ("formulario_seccion/", formulario_seccion, name="formulario_seccion"),
    path ("buscar/",  buscar),
    path ("busqueda/", busqueda, name="busqueda"),
    path("login/", MyLogin.as_view(), name="login"),
    path("logout/",LogoutView.as_view(template_name="Blog/logout.html"),name="Logout"),
    path("registro/", register, name="registro"),
    #editarperfil
    path("editar-perfil/", editar_perfil, name="EditarPerfil")


    ]   