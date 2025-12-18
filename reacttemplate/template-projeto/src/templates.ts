interface DataAluno {
  nome: string;
  idade: number;
  data_de_ingresso: string;
}

interface AlunosPorCurso{
  curso: string;
  alunos: DataAluno[];
}

interface Matricula{
  aluno: string;
  curso: string;
  numero_da_matricula: number;
  data_da_matricula: string;
  status: string; // "paga" ou "pendente"
  status_aluno: string;
  nota_final: number;
}

interface Curso {
  nome_curso: string;
  duracao: number;
  modalidade: string;
  carga_horaria: number;
  valor_de_inscricao: string;
  status: string; // "ativo" ou "inativo"
}

interface CursosPorAluno{
  aluno: string;
  cursos: Curso[];
}

interface CursosAtivos {
  nome_curso: string;
  duracao: number;
  modalidade: string;
  carga_horaria: number;
  valor_de_inscricao: string;
  status: string; // "ativo" ou "inativo"
}

interface TotalDeAlunos {
  total_de_alunos: number;
}

interface TotalPagoPorAluno {
  aluno: string;
  total_pago: number;
}

interface TotalDevidoPorAluno {
  aluno: string;
  total_devido: number;
}

interface MatriculasPendentes{
  matriculas: Matricula[];
}

interface MatriculasPagasVsPendentes {
  matriculas_pagas: number;
  matriculas_pendentes: number;
}

export type {
  AlunosPorCurso,
  CursosAtivos,
  TotalDeAlunos,
  MatriculasPagasVsPendentes,
  TotalPagoPorAluno,
  TotalDevidoPorAluno,
  MatriculasPendentes,
  CursosPorAluno
};