# Generated by Django 2.2.5 on 2019-09-08 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuadronvialapi', '0005_auto_20190907_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField(default=0)),
            ],
        ),
    ]
