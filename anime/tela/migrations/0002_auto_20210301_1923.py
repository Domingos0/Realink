# Generated by Django 3.1.7 on 2021-03-01 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tela', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Cód.')),
                ('site_nome', models.CharField(default='', max_length=200, verbose_name='Nome do Site')),
            ],
        ),
        migrations.DeleteModel(
            name='Tela',
        ),
    ]
