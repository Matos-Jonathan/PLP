class Curso:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def remover_disciplina(self, disciplina):
        self.disciplinas.remove(disciplina)

    def listar_disciplinas(self):
        return self.disciplinas

    def __str__(self):
        return  f"{self.codigo} - {self.nome}"