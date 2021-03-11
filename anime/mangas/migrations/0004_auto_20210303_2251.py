# Generated by Django 3.1.7 on 2021-03-04 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0003_auto_20210303_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='mangas',
            name='categoria',
            field=models.CharField(choices=[('manga', 'Manga'), ('anime', 'Anime'), ('novel', 'Novel')], default='', max_length=200, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='mangas',
            name='nome_genero',
            field=models.CharField(default='', max_length=200, verbose_name='Genero'),
        ),
    ]