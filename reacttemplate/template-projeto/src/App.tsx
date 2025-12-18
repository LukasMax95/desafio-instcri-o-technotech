import { useState, useEffect, type SetStateAction, use } from 'react'
import reactLogo from './assets/react.svg'
import axios from 'axios'
import type { AlunosPorCurso, CursosAtivos, TotalDeAlunos, MatriculasPagasVsPendentes } from './templates'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [items, setItems] = useState<AlunosPorCurso[]>([]);
  const [nome_curso, setNomeCurso] = useState<string>('');
  const [items2, setItems2] = useState<CursosAtivos[]>([]);
  const [totalAlunos, setTotalAlunos] = useState<TotalDeAlunos | null>(null);
  const [matriculasStatus, setMatriculasStatus] = useState<MatriculasPagasVsPendentes[]>([]);
  

  const handleChange = (evento: { target: { value: SetStateAction<string> } }) => {
    // Atualizar o estado com o valor atual do input
    setNomeCurso(evento.target.value);
    console.log(nome_curso);
  };


  // verificar se o localhost do backend é 8000 ou 8001

  const getAlunosPorCurso = () => {
    axios.get<AlunosPorCurso[]>(`http://127.0.0.1:8000/api/v1/relatorios/alunos-por-curso/${nome_curso}/`)
      .then(response => {
        console.log([response.data]);
        console.log(items2);
        console.log(totalAlunos);
        setItems([response.data]);
        console.log(items);
      })
      .catch(error => {
        console.error('Erro ao buscar dados:', error);
      });
  }

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
      </div>
    </>
  )
}

export default App;
