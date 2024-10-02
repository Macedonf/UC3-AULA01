from flask import Flask, render_template, request
import mensagens

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        #Obtém o nome do formulário
        nome = request.form.get("nome") #atributo name do formulário

        #gera msg
        mensagem = f"Olá{nome}!\nMensagem: {mensagens.obter_mensagem_aleatoria()}"

        #renderizar pagina com msg
        return render_template("index.html" , texto = mensagem)


    return render_template("index.html")

if __name__=="__main__":
  app.run(debug= True)


  # verbos
  # GET - responsavel por chamadas simples, url
  # POST - responsável por chamadas complexas, salvamento de dados e etc.
  # PATCH - alterar pedaço da informação
  # DELETE - Deletar dadaos
  # PUT - Alterar todos os dados