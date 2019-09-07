from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length = 100)
		
class Pregunta(models.Model):
	pregunta = models.CharField(max_length = 500)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	

