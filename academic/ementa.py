class Ementa:
    def __init__(self, descricao):
        self.descricao = descricao

    def __getDescricao(self):
        return self.descricao
    
    def __setDescricao(self, descricao):
        self.descricao = descricao