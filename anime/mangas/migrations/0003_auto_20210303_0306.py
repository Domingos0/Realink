# Generated by Django 3.1.7 on 2021-03-03 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0002_auto_20210303_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mangas',
            name='nome_genero',
            field=models.CharField(default='', max_length=200, verbose_name='genero'),
        ),
    ]