from django.contrib import admin

# Register your models here.

from . models import Categoria
from . models import Pregunta
from . models import Respuesta
from . models import Usuario
from . models import Ranking

admin.site.register(Categoria)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Usuario)
admin.site.register(Ranking)
