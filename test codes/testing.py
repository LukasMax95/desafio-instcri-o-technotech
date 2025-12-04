#código base do projeto a ser implementado para o projeto django com fastapi configurado a partir do diretório ./django

#funcionalidades obrigatórias:

class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas
        self.email = f"{nome.lower().replace(' ', '.')}@escola.com"
        self.cpf = "000.000.000-00"  # Placeholder CPF
        self.data_de_ingresso = "2023-01-01"  # Placeholder date

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def esta_aprovado(self):
        media = self.calcular_media()
        return media >= 7
    
class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao  # in months
        self.carga_horaria = duracao * 4 * 5  # assuming 4 weeks/month and 5 hours/week
        self.value_subscription = duracao * 100  # assuming 100 currency units per month
        self.status = "Ativo"

    def descricao(self):
        return f"Curso: {self.nome}, Duração: {self.duracao} meses"
    
class Matricula:
    def __init__(self, aluno, curso):
        self.aluno = aluno
        self.curso = curso
        self.data_de_matricula = "2023-01-15"  # Placeholder date
        self.status = "Ativa"

    def detalhes_matricula(self):
        return f"Aluno: {self.aluno.nome}, Curso: {self.curso.nome}, Data de Matrícula: {self.data_de_matricula}"

class Financeiro:
    def __init__(self, matricula):
        self.matricula = matricula
        self.valor_total = matricula.curso.value_subscription
        self.valor_pago = 0

    def registrar_pagamento(self, valor):
        self.valor_pago += valor

    def saldo_devedor(self):
        return self.valor_total - self.valor_pago

class Relatorio:
    @staticmethod
    def gerar_relatorio_aluno(aluno):
        return {
            "Nome": aluno.nome,
            "Idade": aluno.idade,
            "Média": aluno.calcular_media(),
            "Aprovado": aluno.esta_aprovado()
        }

    @staticmethod
    def gerar_relatorio_curso(curso):
        return {
            "Nome do Curso": curso.nome,
            "Duração (meses)": curso.duracao,
            "Carga Horária": curso.carga_horaria,
            "Valor da Mensalidade": curso.value_subscription,
            "Status": curso.status
        }
    
