from flask import Blueprint, render_template, request, url_for, redirect
from services.bike_service import BikeService

bike_blueprint: Blueprint = Blueprint('bike', __name__)
bike_service = BikeService()

# Route for listing all bikes
@bike_blueprint.route("/")
def index():
    bicicletas = bike_service.listar_bicicleta()
    return render_template("index.html", bicicletas=bicicletas)

# Route for adding a new bike
@bike_blueprint.route("/adicionarBicicleta", methods=["POST"])
def adicionar_bicicleta():
    modelo = request.form.get("modelo")
    categoria = request.form.get("categoria")
    preco = request.form.get("preco")
    status = request.form.get("status")  # Mantenha assim

    try:
        bike_service.incluir_bicicleta(modelo, categoria, preco, status)  # Mantenha assim
    except ValueError as e:
        return str(e), 400

    return redirect(url_for("bike.index"))

# Route for marking a bike as unavailable (e.g., sold)
@bike_blueprint.route("/indisponibilizarBicicleta/<int:bicicleta_id>")
def indisponibilizar(bicicleta_id):
    try:
        bike_service.vender_bicicleta(bicicleta_id)
    except ValueError as e:
        return str(e), 400
    return redirect(url_for("bike.index"))

@bike_blueprint.route("/removerBicicleta/<int:bicicleta_id>")
def remover(bicicleta_id):
    try:
        bike_service.remover_bicicleta(bicicleta_id)
    except ValueError as e:
        return str(e), 400
    return redirect(url_for("bike.index"))
