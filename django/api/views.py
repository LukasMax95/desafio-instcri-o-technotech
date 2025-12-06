from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Aluno, Curso, Matricula
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunoListCreate(APIView):
    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CursoListCreate(APIView):
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MatriculaListCreate(APIView):
    def get(self, request):
        matriculas = Matricula.objects.all()
        serializer = MatriculaSerializer(matriculas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MatriculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#operações financeiras
#listar matriculas com status
#total devido por aluno
#total pago pelo aluno

# financeiro views version (listar matriculas com status "pendente", total pago por aluno, total devido por aluno, cursos por aluno)
class MatriculaPendenteListView(APIView):
    def get(self, request):
        matriculas_pendentes = Matricula.objects.filter(status="pendente")
        serializer = MatriculaSerializer(matriculas_pendentes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#obs: obter o valor do curso a partir da chave estrangeira na matricula
class TotalPagoPorAlunoView(APIView):
    def get(self, request, nome_aluno):
        try:
            aluno = Aluno.objects.get(nome=nome_aluno)

        except Aluno.DoesNotExist:
            return Response({'error': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        curso = Curso.objects.get(matricula__aluno=aluno)
        total_pago = Matricula.objects.filter(aluno=aluno, status="pago").count() * curso.valor_de_inscricao
        return Response({'aluno': aluno.nome, 'total_pago': total_pago}, status=status.HTTP_200_OK)

    
class TotalDevidoPorAlunoView(APIView):
    def get(self, request, nome_aluno):
        try:
            aluno = Aluno.objects.get(nome=nome_aluno)
        except Aluno.DoesNotExist:
            return Response({'error': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        curso = Curso.objects.get(matricula__aluno=aluno)
        total_devido = Matricula.objects.filter(aluno=aluno, status="pendente").count() * curso.valor_de_inscricao
        return Response({'aluno': aluno.nome, 'total_devido': total_devido}, status=status.HTTP_200_OK)
    
class CursosPorAlunoView(APIView):
    def get(self, request, nome_aluno):
        try:
            aluno = Aluno.objects.get(nome=nome_aluno)
        except Aluno.DoesNotExist:
            return Response({'error': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        matriculas = Matricula.objects.filter(aluno=aluno)
        cursos = [matricula.curso for matricula in matriculas]
        serializer = CursoSerializer(cursos, many=True)
        return Response({'aluno': aluno.nome, 'cursos': serializer.data}, status=status.HTTP_200_OK)

# relatórios views version (listar alunos por curso, total de alunos, listar cursos ativos, matriculas pagas vs pendentes)
class AlunosPorCursoView(APIView):
    def get(self, request, nome_curso):
        try:
            curso = Curso.objects.get(nome_curso=nome_curso)
        except Curso.DoesNotExist:
            return Response({'error': 'Curso não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        matriculas = Matricula.objects.filter(curso=curso)
        alunos = [matricula.aluno for matricula in matriculas]
        serializer = AlunoSerializer(alunos, many=True)
        return Response({'curso': curso.nome_curso, 'alunos': serializer.data}, status=status.HTTP_200_OK)
    
class TotalDeAlunosView(APIView):
    def get(self, request):
        total_alunos = Aluno.objects.count()
        return Response({'total_de_alunos': total_alunos}, status=status.HTTP_200_OK)

class CursosAtivosView(APIView):
    def get(self, request):
        cursos_ativos = Curso.objects.filter(status="ativo")
        serializer = CursoSerializer(cursos_ativos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MatriculasPagasVsPendentesView(APIView):
    def get(self, request):
        total_pagas = Matricula.objects.filter(status="pago").count()
        total_pendentes = Matricula.objects.filter(status="pendente").count()
        return Response({'matriculas_pagas': total_pagas, 'matriculas_pendentes': total_pendentes}, status=status.HTTP_200_OK)
    
# histórico do aluno (cursos matriculados, status, totais)
class HistoricoDoAlunoView(APIView):
    def get(self, request, nome_aluno):
        try:
            aluno = Aluno.objects.get(nome=nome_aluno)
        except Aluno.DoesNotExist:
            return Response({'error': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        matriculas = Matricula.objects.filter(aluno=aluno)
        serializer = MatriculaSerializer(matriculas, many=True)
        return Response({'aluno': aluno.nome, 'historico': serializer.data}, status=status.HTTP_200_OK)

class AlunoList(APIView):
    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

class AlunoDetail(APIView):
    def get_object(self, nome):
        try:
            return Aluno.objects.get(nome=nome)
        except Aluno.DoesNotExist:
            return None

    def get(self, request, nome):
        aluno = self.get_object(nome)
        if aluno is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)    