CREATE DATABASE meu_database;
\c meu_database;

CREATE Table Alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE Table Cursos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    status_ativo BOOLEAN NOT NULL,
    descricao TEXT
);

CREATE Table Matriculas (
    id SERIAL PRIMARY KEY,
    aluno_id INT REFERENCES Alunos(id),
    curso_id INT REFERENCES Cursos(id),
    status_aluno VARCHAR(50) NOT NULL,
    status_pago BOOLEAN NOT NULL,
    data_matricula DATE NOT NULL
);

INSERT INTO Alunos (nome, idade, email) VALUES
('João Silva', 20, 'joaosilva@mail.com'),
('Maria Oliveira', 22, 'mariaoliveira@mail.com'),
('Pedro Santos', 19, 'pedrosantos@mail.com'),
('Ana Costa', 21, 'anacosta@mail.com'),
('Lucas Pereira', 23, 'lucaspereira@mail.com');

INSERT INTO Cursos (titulo, valor, status_ativo, descricao) VALUES
('Introdução à Programação', 49.99, TRUE, 'Curso básico de programação para iniciantes.'),
('Desenvolvimento Web', 79.99, TRUE, 'Aprenda a criar sites e aplicações web.'),
('Data Science', 99.99, FALSE, 'Curso avançado sobre análise de dados e machine learning.'),
('Design Gráfico', 59.99, TRUE, 'Fundamentos do design gráfico e uso de ferramentas.'),
('Marketing Digital', 69.99, TRUE, 'Estratégias de marketing no ambiente digital.');

INSERT INTO Matriculas (aluno_id, curso_id, status_aluno, status_pago, data_matricula) VALUES
(1, 1, 'ativo', TRUE, '2023-01-15'),
(1, 2, 'ativo', FALSE, '2023-02-20'),
(2, 2, 'inativo', TRUE, '2023-03-10'),
(2, 3, 'ativo', FALSE, '2023-04-05'),
(3, 1, 'ativo', TRUE, '2023-01-25'),
(3, 4, 'ativo', TRUE, '2023-02-15'),
(4, 5, 'inativo', FALSE, '2023-03-30'),
(5, 4, 'ativo', TRUE, '2023-04-12'),
(5, 2, 'ativo', FALSE, '2023-05-01');

-- exibir as tabelas
SELECT * FROM Alunos;
SELECT * FROM Cursos;
SELECT * FROM Matriculas;

-- listar matriculas com status "ativo" e valor maior que 50.00
SELECT * FROM Matriculas
WHERE status_aluno = 'ativo' AND curso_id IN (
    SELECT id FROM Cursos WHERE valor > 50.00
);

-- valor total devido por cada aluno
SELECT a.nome, SUM(c.valor) AS total_devido
FROM Alunos a
JOIN Matriculas m ON a.id = m.aluno_id
JOIN Cursos c ON m.curso_id = c.id
WHERE m.status_pago = FALSE
GROUP BY a.nome;

-- total pago por cada aluno
SELECT a.nome, SUM(c.valor) AS total_pago
FROM Alunos a
JOIN Matriculas m ON a.id = m.aluno_id
JOIN Cursos c ON m.curso_id = c.id
WHERE m.status_pago = TRUE
GROUP BY a.nome;

-- Histórico do aluno
-- cursos matriculados
SELECT a.nome, c.titulo, m.status_aluno, m.status_pago, m.data_matricula
FROM Alunos a
JOIN Matriculas m ON a.id = m.aluno_id
JOIN Cursos c ON m.curso_id = c.id
WHERE a.id = 1; -- substitua 1 pelo ID do aluno desejado
-- status
SELECT status_aluno, COUNT(*) AS quantidade
FROM Matriculas
WHERE aluno_id = 1 -- substitua 1 pelo ID do aluno desejado
GROUP BY status_aluno;
-- totais
SELECT 
    SUM(CASE WHEN status_pago = TRUE THEN c.valor ELSE 0 END) AS total_pago,
    SUM(CASE WHEN status_pago = FALSE THEN c.valor ELSE 0 END) AS total_devido
FROM Matriculas m
JOIN Cursos c ON m.curso_id = c.id
WHERE m.aluno_id = 1; -- substitua 1 pelo ID do aluno desejado

-- dashbord geral
-- total de alunos
SELECT COUNT(*) AS total_alunos FROM Alunos;
-- cursos ativos
SELECT COUNT(*) AS cursos_ativos FROM Cursos WHERE status_ativo = TRUE;
-- matriculas pagas vs pendentes
SELECT 
    SUM(CASE WHEN status_pago = TRUE THEN 1 ELSE 0 END) AS matriculas_pagas,
    SUM(CASE WHEN status_pago = FALSE THEN 1 ELSE 0 END) AS matriculas_pendentes
FROM Matriculas;
-- receita total
SELECT SUM(c.valor) AS receita_total
FROM Matriculas m
JOIN Cursos c ON m.curso_id = c.id
WHERE m.status_pago = TRUE;