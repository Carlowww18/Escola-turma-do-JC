from django.db import models
from datetime import date

class Aluno(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
    endereco = models.CharField(max_length=12, null=True)
    cpf = models.CharField(max_length=14, null=True, verbose_name='CPF')
    telefone = models.CharField(max_length=16, null=True)
    data_nascimento = models.DateField(blank = True, null = True)
    sexo_choices = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )
    sexo = models.CharField(max_length=1, default=None, choices=sexo_choices, blank=True, null=True)
    email = models.EmailField()
    matricula = models.CharField(max_length=15, blank=True, null=True, unique=True)
    idade = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.data_nascimento:
            hoje = date.today()
            self.idade = hoje.year - self.data_nascimento.year - (
                (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day)
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_completo


class Administrador(models.Model):
    nome = models.CharField(max_length=50, null=True)
    cpf = models.CharField(max_length=14, null=True, verbose_name='CPF')
    telefone = models.CharField(max_length=15, blank=True, null=True)   
    data_nascimento = models.DateField(null=True, blank=True)
    endereco = models.TextField(blank=True, null=True)
    cargo = models.CharField(max_length=50)
    data_cadastro = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.data_cadastro:
            self.data_cadastro = date.today()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Administradore'

    def __str__(self):
        return f'{self.nome}-({self.cargo})'