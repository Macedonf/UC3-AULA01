from flask import Flask
#from flask_sqlalchemy import SQLALchemy
from controllers.task_controller import task_blueprint

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://task.db]'
#app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.register_blueprint(task_blueprint)

if __name__ == '__main__':
    app.run(debug=True)