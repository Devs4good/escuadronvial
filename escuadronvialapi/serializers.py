from rest_framework import serializers

from .models import Categoria


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Categoria
		fields = ["url", "nombre", "id"]