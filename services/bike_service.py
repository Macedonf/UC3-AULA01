from models.bike_model import Bike

class BikeService:

    def __init__(self):
        self.bicicletas = []

    def incluir_bicicleta(self, modelo, categoria, preco, status):
        # Validações básicas para cada campo
        if not modelo:
            raise ValueError("O campo modelo não pode ser vazio")
        if not categoria:
            raise ValueError("O campo categoria não pode ser vazio")
        if not preco:
            raise ValueError("O campo preço não pode ser vazio")
        if not status:
            raise ValueError("O campo status não pode ser vazio")

        # Criação de uma nova instância de bicicleta com todos os atributos
        nova_bicicleta = Bike(modelo, categoria, preco, status == "disponivel")

        # Adiciona a nova bicicleta na lista
        self.bicicletas.append(nova_bicicleta)

    def listar_bicicleta(self):
        return self.bicicletas

    def vender_bicicleta(self, bicicleta_id):
        # Marca a bicicleta como vendida/indisponível
        if 0 <= bicicleta_id < len(self.bicicletas):
            self.bicicletas[bicicleta_id].disponivel = False
        else:
            raise ValueError(f"Bicicleta com ID {bicicleta_id} não encontrada")

    def remover_bicicleta(self, bicicleta_id):
        # Remove a bicicleta da lista por ID
        if 0 <= bicicleta_id < len(self.bicicletas):
            self.bicicletas.pop(bicicleta_id)
        else:
            raise ValueError(f"Bicicleta com ID {bicicleta_id} não encontrada")
