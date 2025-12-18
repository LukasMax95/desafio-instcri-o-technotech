import { useState, useEffect, type SetStateAction, use } from 'react'
import reactLogo from './assets/react.svg'
import axios from 'axios'
import type { 
  AlunosPorCurso, 
  CursosAtivos, 
  TotalDeAlunos, 
  MatriculasPagasVsPendentes, 
  TotalPagoPorAluno,
  TotalDevidoPorAluno,
  MatriculasPendentes,
  CursosPorAluno
 } from './templates'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [items, setItems] = useState<AlunosPorCurso[]>([]);
  const [nome_curso, setNomeCurso] = useState<string>('');
  const [nome_aluno, setNomeAluno] = useState<string>('');
  const [items2, setItems2] = useState<CursosAtivos[]>([]);
  const [totalAlunos, setTotalAlunos] = useState<TotalDeAlunos | null>(null);
  const [totalPagoPorAluno, setTotalPagoPorAluno] = useState<TotalPagoPorAluno | null>(null);
  const [totalDevidoPorAluno, setTotalDevidoPorAluno] = useState<TotalDevidoPorAluno | null>(null);
  const [matriculasPendentes, setMatriculasPendentes] = useState<MatriculasPendentes[] | null>(null);
  const [cursosPorAluno, setCursosPorAluno] = useState<CursosPorAluno | null>(null);
  const [matriculasStatus, setMatriculasStatus] = useState<MatriculasPagasVsPendentes[]>([]);
  

  const handleChange = (evento: { target: { value: SetStateAction<string> } }) => {
    // Atualizar o estado com o valor atual do input
    setNomeCurso(evento.target.value);
    console.log(nome_curso);
  };

  const handleChange2 = (evento: { target: { value: SetStateAction<string> } }) => {
    // Atualizar o estado com o valor atual do input
    setNomeAluno(evento.target.value);
    console.log(nome_aluno);
  };

  const fetchCursosporAluno = () => {
    axios.get<CursosPorAluno>(`http://127.0.0.1:8000/api/v1/financeiro/cursos-por-aluno/${nome_aluno}/`)
      .then(response => {
        console.log(response.data);
        setCursosPorAluno(response.data);
      })
      .catch(error => {
        console.error('Erro ao buscar cursos por aluno:', error);
      });
  }

  const fetchMatriculasPendentes = () => {
    axios.get<MatriculasPendentes[]>('http://127.0.0.1:8000/api/v1/financeiro/matriculas-pendentes/')
      .then(response => {
        console.log(response.data);
        setMatriculasPendentes(response.data);
      })
      .catch(error => {
        console.error('Erro ao buscar matriculas:', error);
      });
  };

  const financeiroGetAluno = () =>{
    // primeiro total pago, depois total devido
    axios.get<TotalPagoPorAluno>(`http://127.0.0.1:8000/api/v1/financeiro/total-pago/${nome_aluno}/`)
      .then(response => {
        console.log(response.data);
        setTotalPagoPorAluno(response.data);
      })
      .catch(error => {
        console.error('Erro ao buscar total pago:', error);
      });
    axios.get<TotalDevidoPorAluno>(`http://127.0.0.1:8000/api/v1/financeiro/total-devido/${nome_aluno}/`)
      .then(response => {
        console.log(response.data);
        setTotalDevidoPorAluno(response.data);
      })
      .catch(error => {
        console.error('Erro ao buscar total devido:', error);
      });
  }
  // verificar se o localhost do backend é 8000 ou 8001

  const getAlunosPorCurso = () => {
    axios.get<AlunosPorCurso[]>(`http://127.0.0.1:8000/api/v1/relatorios/alunos-por-curso/${nome_curso}/`)
      .then(response => {
        console.log([response.data]);
        setItems([response.data]);
      })
      .catch(error => {
        console.error('Erro ao buscar dados:', error);
      });
  }

  useEffect(() =>{
    axios.get<MatriculasPagasVsPendentes[]>('http://127.0.0.1:8000/api/v1/relatorios/matriculas-pagas-vs-pendentes/')
      .then(response => {
        console.log(response.data);
        setMatriculasStatus(response.data);
      }).catch(error =>{
        console.error(`erro ao buscar matriculas: ${error}`)
      });
  }, []);

  useEffect(() => {
    // Buscar Cursos Ativos
    axios.get<CursosAtivos[]>('http://127.0.0.1:8000/api/v1/relatorios/cursos-ativos/')
      .then(response => {
        setItems2(response.data);
      })
      .catch(error => {
        alert(`Erro ao buscar cursos ativos: ${error}`);
        console.error('Erro ao buscar cursos ativos:', error);
      });
    }, []);
  
    useEffect(() => {
      // Buscar Total de Alunos
      axios.get<TotalDeAlunos>('http://127.0.0.1:8000/api/v1/relatorios/total-de-alunos/')
        .then(response => {
          setTotalAlunos(response.data);
        })
        .catch(error => {
          console.error('Erro ao buscar total de alunos:', error);
        });
    }, []);
  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>

      <h1>Templates HTML para backend SQLITE django</h1>
      <div className="card">
        <h1>Seção 01: Financeiro</h1>
        <input type='text'
          onChange={handleChange2}/>
        <button onClick={financeiroGetAluno}>Total Pago/Devido</button>
        <div className='aluno-info'>
          <h3>Aluno: {nome_aluno}</h3>
          {totalPagoPorAluno ? `Total Pago: R$ ${totalPagoPorAluno.total_pago}` : 'Carregando...'}
          <br/>
          {totalDevidoPorAluno ? `Total Devido: R$ ${totalDevidoPorAluno.total_devido}` : 'Carregando...'}
        </div>
        <h3>Matriculas Pendentes</h3>
        <button onClick={fetchMatriculasPendentes}>Buscar Matriculas Pendentes</button>
        <div className = 'matriculas-pendentes'>
        <ul className='sem_ponto'>
        {matriculasPendentes?.map((item, index) => (
          <li key={index}>
            <div className='matricula-info'>
              <b>Aluno:</b> {item.aluno} <br/>
              <b>Curso:</b> {item.curso} <br/>
              <b>Número da Matrícula:</b> {item.numero_da_matricula} <br/>
              <b>Data da Matrícula:</b> {item.data_de_matricula} <br/>
              <b>Status Financeiro:</b> {item.status} <br/>
              <b>Status do Aluno:</b> {item.status_aluno} <br/>
            </div>
          </li>
        ))}
      </ul>
      </div>
      <h3>Cursos por Aluno</h3>
      <input type='text'
          onChange={handleChange}/>
        <button onClick={fetchCursosporAluno}>Buscar Cursos</button>
      <div className='matriculas-pendentes'>
        {cursosPorAluno && (
          <div>
            <h3>Aluno: {cursosPorAluno.aluno}</h3>
            <h4>Cursos:</h4>
            <ul className='sem_ponto'>
              {cursosPorAluno.cursos.map((curso, index) => (
                <li key={index}>
                  <div className='curso-info'>
                    <b>Nome do Curso:</b> {curso.nome_curso} <br/>
                    <b>Duração:</b> {curso.duracao} meses<br/>
                    <b>Modalidade:</b> {curso.modalidade} <br/>
                    <b>Carga Horária:</b> {curso.carga_horaria} horas<br/>
                    <b>Valor de Inscrição:</b> {curso.valor_de_inscricao} <br/>
                    <b>Status:</b> {curso.status} <br/>
                  </div>
                </li>
              ))}</ul>
          </div>
        )}
      </div>
      </div>
      <div className="card">
        <h1>Seção 02: Relatórios</h1>
        <h2>Alunos por Curso: React</h2>
        <input type='text'
          onChange={handleChange}/>
        <button onClick={getAlunosPorCurso}>Buscar Alunos por Curso</button>
        <ul className="sem_ponto">{items.map ((item, index) => (
          <li key={index}>
            <div className='aluno-curso-info'>
            Curso: {item.curso}<br/>
            <h3>Alunos:</h3>
            {item.alunos.map((aluno, idx) => (
              <div key={idx} className='aluno-info'>
                <b>Nome do Aluno:</b> {aluno.nome}<br/>
                <b>Idade:</b> {aluno.idade}<br/>
                <b>Data de Ingresso:</b> {aluno.data_de_ingresso}
              </div>
            ))}
            </div>
          </li>
          
        ))}</ul>
        <h2> Cursos Ativos </h2>
        <ul className='sem_ponto'>
          {items2.map((item, index) => (
            <li key={index}>
              <div className='curso-info'>
              <b>Curso:</b> {item.nome_curso}<br/>
              <b>Duração:</b> {item.duracao} meses<br/>
              <b>Modalidade:</b> {item.modalidade}<br/>
              <b>Carga Horária:</b> {item.carga_horaria} horas<br/>
              <b>Valor de Inscrição:</b> {item.valor_de_inscricao}<br/>
              <b>Ativo:</b> {item.status}
              </div>
            </li>
          ))}
        </ul>
          <h2> Total de Alunos </h2>
          <div className='aluno-info'>
            {totalAlunos ? `Total de Alunos: ${totalAlunos.total_de_alunos}` : 'Carregando...'}
          </div>

          <h2>Matriculas Pagas vs Pendentes</h2>
          <div className='aluno-info'>
            {`Matriculas pagas: ${matriculasStatus.matriculas_pagas}`}<br/>
            {`Matriculas pendentes: ${matriculasStatus.matriculas_pendentes}`}
          </div>
      </div>
    </>
  )
}

export default App;
