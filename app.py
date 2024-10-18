from flask import Flask, redirect, url_for
from configurations.database import db
from controllers.bike_controller import bike_blueprint
from dotenv import load_dotenv
from urllib.parse import quote
import os

app = Flask(__name__)
app.register_blueprint(bike_blueprint)

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')

# Converte a senha para bytes antes de usar quote
password = quote(password.encode('utf-8'))

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# Corrigido para db.init_app(app) em vez de db,init_app(app)
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
