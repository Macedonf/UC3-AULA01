from configurations.database import db
from models.bike_model import Bike
from sqlalchemy import text


class BikeRepository:
    @staticmethod
    def get_all_bikes():
        query = text("SELECT * FROM bikes")
        result = db.session.execute(query)
        return result.fetchall()

    @staticmethod
    def add_bike(modelo, categoria, preco, status):
        query = text("""
            INSERT INTO bikes (modelo, categoria, preco, status)
            VALUES (:modelo, :categoria, :preco, :status)
        """)

        db.session.execute(query, {
            'modelo': modelo,
            'categoria': categoria,
            'preco': preco,
            'status': status
        })

        db.session.commit()

    @staticmethod
    def indisponibilizar_bike(bicicleta_id):
        print(f'>>>>>>>> {bicicleta_id}')
        query = text("UPDATE bikes SET completa = TRUE WHERE id = :id")
        db.session.execute(query, {'id': bicicleta_id})
        db.session.commit()

    @staticmethod
    def delete_bike(bicicleta_id):
        query = text("DELETE FROM bikes WHERE id = :id")
        db.session.execute(query, {'id': bicicleta_id})
        db.session.commit()
