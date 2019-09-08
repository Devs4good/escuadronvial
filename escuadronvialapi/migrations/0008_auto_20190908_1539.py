# Generated by Django 2.2.5 on 2019-09-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuadronvialapi', '0007_preguntausuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntausuario',
            name='categoria',
        ),
        migrations.AddField(
            model_name='preguntausuario',
            name='respuesta',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='preguntausuario',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
