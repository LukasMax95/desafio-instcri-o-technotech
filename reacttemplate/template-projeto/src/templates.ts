interface AlunosPorCurso {
  nome_curso: string;
  total_alunos: number;
}

interface CursosAtivos {
  nome_curso: string;
  ativo: boolean;
}

interface TotalDeAlunos {
  total_alunos: number;
}

interface MatriculasPagasVsPendentes {
  curso: string;
  matriculas_pagas: number;
  matriculas_pendentes: number;
}

export type {
  AlunosPorCurso,
  CursosAtivos,
  TotalDeAlunos,
  MatriculasPagasVsPendentes
};