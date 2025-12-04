from django.contrib import admin
from .models import Aluno, Curso, Matricula
# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'idade', 'cpf', 'data_de_ingresso')
    search_fields = ('nome', 'email', 'cpf')
    ordering = ('nome',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome_curso', 'duracao', 'modalidade', 'carga_horaria', 'valor_de_inscricao', 'status')
    search_fields = ('nome_curso', 'modalidade', 'status')
    ordering = ('nome_curso',)

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('numero_da_matricula', 'aluno', 'curso', 'data_de_matricula', 'status', 'status_aluno', 'nota')
    search_fields = ('aluno__nome', 'curso__nome_curso', 'status', 'status_aluno')
    ordering = ('-data_de_matricula',)