# Generated by Django 5.0.7 on 2024-08-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_rename_endereço_aluno_endereco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='aluno',
            name='endereco',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='idade',
            field=models.IntegerField(null=True),
        ),
    ]
