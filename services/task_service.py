from flask import render_template

from models.task_model import Task
from app import db

class TaskService:

    def adicionar_tarefa(self, conteudo,  prioridade = "Média"): # conteudo é uma str que tem a descrição/titulo da tarefa
        if not conteudo:
            raise ValueError("A tarefa não pode ser vazia")

        nova_tarefa = Task(conteudo=conteudo, prioridade=prioridade) # Task(conteudo, False) é a instanciação da classe Task
        db.session.add(nova_tarefa)
        db.session.commit()

    def listar_tarefas(self):
        return Task.query.all()  #select*from task

    #select * from tasks where completa = false and prioridade in ('Alta', 'Media')


    def completar_tarefa(self, tarefa_id):
        tarefa = Task.query.get(tarefa_id)
        if tarefa:
            tarefa.completar()
            db.session.commit(tarefa)
        else:
            raise Exception("Tarefa não encontrada")

            #db.update = substitui todo o arquivo
         #db commit=salva alterção

    def remover_tarefa(self, tarefa_id):
       tarefa=Task.query.get(tarefa_id)
       if tarefa:
           db.session.delete(tarefa)
           db.session.commit()
       else:
           raise Exception("Tarefa não encotrada")

