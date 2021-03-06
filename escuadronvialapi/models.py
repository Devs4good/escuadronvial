from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Pregunta(models.Model):
    pregunta = models.CharField(max_length=500)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.pregunta


class Respuesta(models.Model):
    respuesta = models.CharField(max_length=500)
    correcta = models.BooleanField(default=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    def __str__(self):
        return self.respuesta


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Ranking(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    puntaje = models.IntegerField(default=0)

    def __str__(self):
        return "{usuario}: {categoria} - {puntaje}".format(
            usuario=str(self.usuario),
            categoria=str(self.categoria),
            puntaje=self.puntaje
        )


class Sesion(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)


class PreguntaUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    pregunta = models.CharField(max_length=500)
    respuesta = models.CharField(max_length=500)

    def __str__(self):
        return "{nombre}: {pregunta} - {respuesta}".format(
            nombre=self.nombre,
            pregunta=self.pregunta,
            respuesta=self.respuesta
        )
