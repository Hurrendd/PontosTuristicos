# Generated by Django 4.1.7 on 2023-04-09 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0004_avaliacao_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='foto',
        ),
    ]