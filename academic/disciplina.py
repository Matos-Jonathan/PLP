class Disciplina:
    def __init__(self, codigo, nome, tipo, pre_requisitos, periodo, carga_horaria, ementa):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.pre_requisitos = pre_requisitos
        self.periodo = periodo
        self.carga_horaria = carga_horaria
        self.ementa = ementa

    def __str__(self):
        return f"{self.codigo} - {self.nome}"