#Desenvolver um programa que permita ao usuário enviar mensagens repetidamente até decidir sair. - Descrição: Implemente um loop infinito que peça ao usuário para digitar uma mensagem. Após cada mensagem, pergunte se o usuário deseja continuar ou sair. Use a palavra-chave 'sair' para quebrar o loop. Cada mensagem, juntamente com uma confirmação de recebimento, deve ser exibida na tela.

while True:
    mensagem = input("Digite uma mensagem (ou 'sair' para encerrar): ")
    if mensagem.lower() == 'sair':
        break
    print(f"Mensagem recebida: {mensagem}")
    confirmacao = input("Confirmação de recebimento (s/n): ")
    if confirmacao.lower() == 'n':
        break
print("Programa encerrado.")