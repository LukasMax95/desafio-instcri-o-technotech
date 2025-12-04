from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField(unique=True)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11, unique=True)
    data_de_ingresso = models.DateField()

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
    
class Curso(models.Model):
    nome_curso = models.CharField(max_length=100, primary_key=True)
    duracao = models.IntegerField()  # duração em meses
    modalidade = models.CharField(max_length=50)  # ex: presencial, online
    carga_horaria = models.IntegerField()  # em horas
    valor_de_inscricao = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="inativo")
    
    
    def atualizar_status(self, novo_status):
        self.status = novo_status
        self.save()

    def __str__(self):
        return self.nome_curso
    
    class Meta:
        ordering = ['nome_curso']


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    numero_da_matricula = models.AutoField(primary_key=True)
    data_de_matricula = models.DateField()
    status = models.CharField(max_length=20, default="pendente")
    status_aluno = models.CharField(max_length=20, default="Matriculado")
    nota = models.FloatField(default=0.0)

    def __str__(self):
        return f"Matrícula {self.numero_da_matricula} - {self.aluno.nome} em {self.curso.nome_curso}"
    
    def atualizar_status(self, novo_status):
        self.status = novo_status
        self.save()
    
    def atualizar_status_aluno(self, novo_status):
        self.status_aluno = novo_status
        self.save()
    
    def atribuir_nota(self, nota):
        self.nota = nota
        self.save()
    
    class Meta:
        ordering = ['data_de_matricula']