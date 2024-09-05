# Generated by Django 5.0.7 on 2024-09-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0008_alter_aluno_matricula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, null=True)),
                ('cpf', models.CharField(max_length=14, null=True, verbose_name='CPF')),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('endereco', models.TextField(blank=True, null=True)),
                ('cargo', models.CharField(max_length=50)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
