from django.contrib import admin
from django.urls import path, include
from Blog.views import (
    register,
    MyLogout,
    MyLogin,
    mostrar_inicio,
    mostrar_articulos,
    mostrar_autores,
    mostrar_seccion,
    procesar_formulario_autor,
    procesar_formulario_articulo,
    procesar_formulario_seccion,
    busqueda,
    buscar
)

urlpatterns = [
    path("inicio/",mostrar_inicio),
    path("autor/",mostrar_autores),
    path("articulo/",mostrar_articulos),
    path("seccion/",mostrar_seccion),
    path ("formulario_autor/", procesar_formulario_autor, name="formulario_autor"),
    path ("formulario_articulo/", procesar_formulario_articulo, name="formulario_articulo"),
    path ("formulario_seccion/", procesar_formulario_seccion, name="formulario_seccion"),
    path ("buscar/",  buscar),
    path ("busqueda/", busqueda, name="busqueda"),
    #login, logout,register 
    path("login/", MyLogin.as_view(), name= "Login"),
    path("logout/", MyLogout.as_view(), name= "Logout"),
    path("register/",register, name="Register")
    ]   