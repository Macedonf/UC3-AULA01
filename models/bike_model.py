from configurations.database import db


class Bike(db.Model):

    __tablename__ = "bikes"

    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String, nullable=False)
    preco = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="disponivel")



    def __repr__(self):
        return f"Bike(modelo='{self.modelo}', categoria='{self.categoria}', preco={self.preco}, disponivel={self.disponivel})"


    def indisponibilizar(self):
        self.disponivel = False
