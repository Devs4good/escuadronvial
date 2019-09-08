from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets, views

from .models import Categoria, Pregunta, Sesion, Respuesta, Ranking
from .serializers import CategoriaSerializer, PreguntaSerializer, SesionSerializer, RespuestaSerializer, RankingSerializer


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


class PreguntasList(views.APIView):
    def get(self, request, cat_id):
        categoria = self.__get_categoria(cat_id)
        preguntas = Pregunta.objects.filter(categoria_id=cat_id)

        print()
        print(preguntas)
        print()
        serializer = PreguntaSerializer(preguntas, many=True)

        return Response(serializer.data)

    def __get_categoria(self, categoria_id):
        try:
            return Categoria.objects.filter(pk=categoria_id)
        except Categoria.DoesNotExist:
            raise Http404
