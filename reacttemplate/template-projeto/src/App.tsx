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
        console.log(response.data);
        console.log(items2);
        console.log(totalAlunos);
        setItems(response.data);
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
        <ul>{items.map ((item, index) => (
          <li key={index}>
            Curso: {item.curso} - Nome: {item.alunos.toString()}
          </li>
        ))}</ul>
        <h2> Cursos Ativos </h2>
        <ul>
          {items2.map((item, index) => (
            <li key={index}>
              Curso: {item.nome_curso} - Ativo: {item.status}
            </li>
          ))}
        </ul>
          <h2> Total de Alunos </h2>
          <p>
            {totalAlunos ? `Total de Alunos: ${totalAlunos.total_de_alunos}` : 'Carregando...'}
          </p>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App;
