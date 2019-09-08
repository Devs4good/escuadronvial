from rest_framework import serializers

from .models import Categoria, Pregunta, Sesion, Respuesta, Ranking


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ["url", "nombre", "id"]


class SesionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sesion
        fields = ["url", "nombre", "edad"]


class RespuestaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Respuesta
        fields = ["url", "respuesta", "pregunta", "correcta"]


class PreguntaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pregunta
        fields = ["url", "pregunta"]

class RankingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ranking
		fields = ["usuario", "categoria", "puntaje"]

