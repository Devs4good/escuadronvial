from rest_framework import serializers

from .models import Categoria, Pregunta, Sesion, Respuesta, Ranking, PreguntaUsuario


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ["url", "id", "nombre"]


class SesionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sesion
        fields = ["url", "id", "nombre", "edad"]


class RespuestaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Respuesta
        fields = ["url", "id", "respuesta", "pregunta", "correcta"]


class PreguntaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pregunta
        fields = ["url", "id", "pregunta"]


class PreguntaUsuarioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PreguntaUsuario
		fields = ["nombre", "pregunta", "respuesta"]


class RankingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ranking
		fields = ["usuario", "categoria", "puntaje"]
