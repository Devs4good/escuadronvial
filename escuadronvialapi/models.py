from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length = 100)
		
class Pregunta(models.Model):
	pregunta = models.CharField(max_length = 500)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	estado = models.BooleanField(default=False)
	

class Respuesta(models.Model):
	respuesta = models.CharField(max_length = 500)
	correcta = models.BooleanField(default=False)
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)