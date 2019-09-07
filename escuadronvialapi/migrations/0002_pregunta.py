# Generated by Django 2.2.5 on 2019-09-07 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escuadronvialapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=500)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuadronvialapi.Categoria')),
            ],
        ),
    ]
