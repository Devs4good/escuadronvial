# Generated by Django 2.2.5 on 2019-09-07 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuadronvialapi', '0004_ranking_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pregunta',
            old_name='estado',
            new_name='publicada',
        ),
    ]
