interface DataAluno {
  nome_curso: string;
  idade: number;
  data_de_ingresso: string;
}

interface AlunosPorCurso{
  curso: string;
  alunos: DataAluno[];
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