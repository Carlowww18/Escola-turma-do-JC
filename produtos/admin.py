from django.contrib import admin
from . models import Aluno, Administrador

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'data_nascimento', 'idade')
    readonly_fields = ('idade',)

    def idade(self, obj):
        return obj.idade
    
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'data_cadastro')
    readonly_fields = ('data_cadastro',)

    def data_cadastro(self, obj):
        return obj.data_cadastro

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Administrador, AdministradorAdmin)