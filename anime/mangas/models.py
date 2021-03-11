from django.db import models

class Mangas(models.Model):
    CATEGORIA = (
        ("manga","Manga"),
        ("anime","Anime"),
        ("novel","Novel"),

    )
    id = models.AutoField(primary_key=True, verbose_name= 'Cód.')
    site_nome = models.CharField(default= '', max_length=200, blank=False, null=False, verbose_name='Nome do Site')
    url_nome = models.CharField(default= '', max_length=200, blank=False, null=False, verbose_name='Url do Site')
    nome_genero = models.CharField(default= '', max_length=200, blank=False, null=False, verbose_name='Url da Foto')
    categoria = models.CharField(default = '',max_length=200, blank=False, null=False, verbose_name = 'Categoria',choices = CATEGORIA)

class Meta:
    db_table = 'Mangas_add'
# Create your models here.
