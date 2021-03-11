from django.db import models

class Sus(models.Model):
    id = models.AutoField(primary_key=True, verbose_name= 'Cód.')
    site_nome = models.CharField(default= '', max_length=200, blank=False, null=False, verbose_name='Nome do Site')
    url_nome = models.CharField(default= '', max_length=200, blank=False, null=False, verbose_name='Url do Site')


class Meta:
    db_table = 'tela_sugestão'
# Create your models here.
