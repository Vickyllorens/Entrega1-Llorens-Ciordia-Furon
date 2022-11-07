from django.contrib import admin
from Blog.models import Articulo, Autor , Section, Avatar

# Register your models here.

admin.site.register(Articulo)
admin.site.register(Autor)
admin.site.register(Section)
admin.site.register(Avatar)