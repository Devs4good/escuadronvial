from django.contrib import admin

# Register your models here.

from . models import Categoria, Pregunta, Respuesta, Usuario, Ranking, PreguntaUsuario

admin.site.register(Categoria)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Usuario)
admin.site.register(Ranking)
admin.site.register(PreguntaUsuario)
