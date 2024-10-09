from app import db

class Task(db.Model):

    __tablename__ = 'tasks'

    id = db.Colum(db.integer, primary_key = True)
    conteudo = db.Column(db.string(200), nullable = False)
    completa = db.Column(db.Boolean, defaut = False)
    prioridade = db.Column(db.String(50), default = "Média")


    def __repr__(self):                  # Representação da tarefa
        return f"Tarefa('{self.conteudo}', '{self.completa}' ,'{self.prioridade}')"

    def __str__(self):                  # Representação  da tarefa
        return f"Conteúdo: {self.conteudo}, Completa: {self.completa} , Prioridade: {self.prioridade}"

    def completar(self):
        self.completa = True            #marcar tarefa como completa
