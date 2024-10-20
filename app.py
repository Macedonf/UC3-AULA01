from flask import Flask
from configurations.blueprints import register_blueprints
from configurations.config import Config
from configurations.database import db
from configurations.sql_commands import create_table_tasks, create_table_users, create_root_user

app = Flask(__name__)

#carrega as configurações da config
app.config.from_object(Config)

#Inicializa a conexão com o banco de dados
db.init_app(app)

register_blueprints(app)

if __name__ == '__main__':
    create_table_tasks(app, db)
    create_table_users(app, db)
    create_root_user(app, db)
    app.run(debug=Config.DEBUG)
