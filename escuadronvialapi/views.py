from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets, views

from .models import Categoria, Pregunta, Sesion, Respuesta, Ranking, PreguntaUsuario
from .serializers import CategoriaSerializer, PreguntaSerializer, SesionSerializer, RespuestaSerializer, RankingSerializer, PreguntaUsuarioSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer


class RespuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer


class RankingViewSet(viewsets.ModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer

class PreguntaUsuarioViewSet(viewsets.ModelViewSet):
	queryset = Ranking.objects.all()
	serializer_class = PreguntaUsuarioSerializer 


class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


class PreguntasList(views.APIView):
    def get(self, request, cat_id):
        preguntas = Pregunta.objects.filter(categoria_id=cat_id)

        print()
        print(preguntas)
        print()
        serializer_context = {
            'request': request,
        }
        serializer = PreguntaSerializer(preguntas, many=True, context=serializer_context)

        return Response(serializer.data)   
