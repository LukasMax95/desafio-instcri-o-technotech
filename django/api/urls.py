from django.urls import path
from .views import AlunoListCreate, CursoListCreate, MatriculaListCreate

urlpatterns = [
    path('alunos/', AlunoListCreate.as_view(), name='aluno-list-create'),
    path('cursos/', CursoListCreate.as_view(), name='curso-list-create'),
    path('matriculas/', MatriculaListCreate.as_view(), name='matricula-list-create'),
]