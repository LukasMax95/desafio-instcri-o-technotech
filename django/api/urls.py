from django.urls import path
from .views import AlunoListCreate, CursoListCreate, MatriculaListCreate
from .views import MatriculaPendenteListView, TotalPagoPorAlunoView, TotalDevidoPorAlunoView, CursosPorAlunoView
from .views import AlunosPorCursoView, CursosAtivosView, TotalDeAlunosView, MatriculasPagasVsPendentesView
urlpatterns = [
    path('alunos/', AlunoListCreate.as_view(), name='aluno-list-create'),
    path('cursos/', CursoListCreate.as_view(), name='curso-list-create'),
    path('matriculas/', MatriculaListCreate.as_view(), name='matricula-list-create'),
    path('financeiro/matriculas-pendentes/', MatriculaPendenteListView.as_view(), name='matricula-pendente-list'),
    path('financeiro/total-pago/<str:nome_aluno>/', TotalPagoPorAlunoView.as_view(), name='total-pago-por-aluno'),
    path('financeiro/total-devido/<str:nome_aluno>/', TotalDevidoPorAlunoView.as_view(), name='total-devido-por-aluno'),
    path('financeiro/cursos-por-aluno/<str:nome_aluno>/', CursosPorAlunoView.as_view(), name='cursos-por-aluno'),
    path('relatorios/alunos-por-curso/<str:nome_curso>/', AlunosPorCursoView.as_view(), name='alunos-por-curso'),
    path('relatorios/total-de-alunos/', TotalDeAlunosView.as_view(), name='total-de-alunos'),
    path('relatorios/cursos-ativos/', CursosAtivosView.as_view(), name='cursos-ativos'),
    path('relatorios/matriculas-pagas-vs-pendentes/', MatriculasPagasVsPendentesView.as_view(), name='matriculas-pagas-vs-pendentes'),
]