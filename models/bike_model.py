class Bike:
    def __init__(self, modelo, categoria, preco, disponivel):
        self.modelo = modelo
        self.categoria = categoria
        self.preco = preco
        self.disponivel = disponivel

    def __repr__(self):
        return f"Bike(modelo='{self.modelo}', categoria='{self.categoria}', preco={self.preco}, disponivel={self.disponivel})"

    def indisponibilizar(self):
        self.disponivel = False
