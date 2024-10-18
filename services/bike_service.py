from repositories.bike_repository import BikeRepository
from configurations.database import db

class BikeService:
    def incluir_bicicleta(self, modelo, categoria, preco, status):  # Alterar de disponivel para status
        if not modelo:
            raise ValueError("O campo modelo não pode ser vazio")
        if not categoria:
            raise ValueError("O campo categoria não pode ser vazio")
        if not preco:
            raise ValueError("O campo preço não pode ser vazio")
        if not status:  # Verifica o status, não disponivel
            raise ValueError("O campo disponibilidade não pode ser vazio")

        BikeRepository.add_bike(modelo, categoria, preco, status) 

    def listar_bicicleta(self):
        return BikeRepository.get_all_bikes()

    def vender_bicicleta(self, bicicleta_id):
        BikeRepository.indisponibilizar_bike(bicicleta_id)

    def remover_bicicleta(self, bicicleta_id):
        BikeRepository.delete_bike(bicicleta_id)
