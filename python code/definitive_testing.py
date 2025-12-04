#Simulação do sistema de testes definitivos para um backend django de uma plataforma de cursos online
class Aluno:
    def __init__(self, nome, email, idade, cpf, data_de_ingresso):
        self.nome = nome #primary key
        self.email = email
        self.idade = idade
        self.cpf = cpf
        self.data_de_ingresso = data_de_ingresso


class Cursos:
    def __init__(self, nome_curso, duracao, modalidade, carga_horaria, valor_de_inscricao, status = "inativo"):
        self.nome_curso = nome_curso #primary key
        self.duracao = duracao
        self.modalidade = modalidade
        self.carga_horaria = carga_horaria
        self.valor_de_inscricao = valor_de_inscricao
        self.status = status
        self.status_aluno = "Matriculado"
        self.nota = 0.0;
    
    def atribuir_nota(self, nota):
        self.nota = nota
    
    def atualizar_status(self, novo_status):
        self.status_aluno = novo_status

class Matricula:
    def __init__(self, aluno, curso, numero_da_matricula, data_de_matricula, status = "pendente"):
        self.aluno = aluno #foreign key
        self.curso = curso #foreign key
        self.numero_da_matricula = numero_da_matricula #primary key
        self.data_de_matricula = data_de_matricula
        self.status = status

import numpy as np
import pandas as pd
class Matriculas:
    def __init__(self):
        self.matriculas = []

    def adicionar_matricula(self, matricula):
        self.matriculas.append(matricula)

    def listar_matriculas(self):
        dados = []
        for matricula in self.matriculas:
            dados.append({
                "Aluno": matricula.aluno.nome,
                "Curso": matricula.curso.nome_curso,
                "Número da Matrícula": matricula.numero_da_matricula,
                "Data de Matrícula": matricula.data_de_matricula,
                "Status": matricula.status
                "Status do Aluno": matricula.curso.status_aluno
            })
        return pd.DataFrame(dados)


class Financeiro:
    def __init__(self):
        self.transacoes = []

    def registrar_aluno(self, aluno, valores_pagos, valores_devidos):
        transacao = {
            "Aluno": aluno.nome,
            "Valores Pagos": valores_pagos,
            "Valores Devidos": valores_devidos
        }
        self.transacoes.append(transacao)
    
    def listar_transacoes(self):
        return pd.DataFrame(self.transacoes)

class Relatorios:
    def __init__(self):
        self.relatorios = []
    
    def historico_aluno(self, aluno, cursos_concluidos, notas_obtidas):
        relatorio = {
            "Aluno": aluno.nome,
            "Cursos Concluídos": cursos_concluidos,
            "Notas Obtidas": notas_obtidas
        }
        self.relatorios.append(relatorio)
    
    def total_cursos(self, cursos):
        total = len(cursos)
        return total
    
    def total_alunos(self, alunos):
        total = len(alunos)
        return total
    
    def total_cursos_ativos(self, cursos):
        total = sum(1 for curso in cursos if curso.status == "ativo")
        return total
    
    def listar_relatorios(self):
        return pd.DataFrame(self.relatorios)