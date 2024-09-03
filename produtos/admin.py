from django.contrib import admin
from . models import Aluno

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'data_nascimento', 'idade')
    readonly_fields = ('idade',)

    def idade(self, obj):
        return obj.idade

admin.site.register(Aluno, AlunoAdmin)