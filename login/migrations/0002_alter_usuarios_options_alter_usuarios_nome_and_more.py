# Generated by Django 5.0.7 on 2024-08-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuarios',
            options={'verbose_name': 'Usuário'},
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nome',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='senha',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
