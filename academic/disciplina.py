class Disciplina:
    def __init__(self, codigo, nome, tipo, periodo, carga_horaria, ementa=None):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.pre_requisitos = []
        self.periodo = periodo
        self.carga_horaria = carga_horaria
        self.ementa = ementa

    def __getCodigo(self):
        return self.codigo
    
    def __setCodigo(self, codigo):
        self.codigo = codigo

    def __getNome(self):
        return self.nome
    
    def __setNome(self, nome):
        self.nome = nome

    def __getTipo(self):
        return self.tipo
    
    def __setTipo(self, tipo):
        self.tipo = tipo

    def __getPreRequisitos(self):
        return self.pre_requisitos

    def __setPreRequisitos(self, preRequisitos):
        self.pre_requisitos.append(preRequisitos)

    def __getCargaHoraria(self):
        return self.carga_horaria
    
    def __setCargaHoraria(self, cargaHoraria):
        self.carga_horaria = cargaHoraria

    def __getPeriodo(self):
        return self.periodo
    
    def __setPeriodo(self, periodo):
        self.periodo = periodo

    def __getEmenta(self):
        return self.ementa.__getDescricao()
    
    def __setEmenta(self, ementa):
        self.ementa = self.ementa.__setDescricao(ementa)

    def __str__(self):
        return f"{self.codigo} - {self.nome}"