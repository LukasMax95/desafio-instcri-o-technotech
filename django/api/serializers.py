from rest_framework import serializers
from .models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'cpf': {'write_only': True},
            'email': {'write_only': True},
        }
        model = Aluno
        fields = ['nome', 'email', 'idade', 'cpf', 'data_de_ingresso']


class CursoSerializer(serializers.ModelSerializer):
    extra_kwargs = {
        'valor_de_inscricao': {'write_only': True},
    }
    class Meta:
        model = Curso
        fields = ['nome_curso', 'duracao', 'modalidade', 'carga_horaria', 'valor_de_inscricao', 'status']


class MatriculaSerializer(serializers.ModelSerializer):
    extra_kwargs = {
        'numero_da_matricula': {'read_only': True},
    }
    class Meta:
        model = Matricula
        fields = ['aluno', 'curso', 'numero_da_matricula', 'data_de_matricula', 'status', 'status_aluno', 'nota']