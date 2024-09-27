numero = float(input("Digite um número: "))

resposta = ""

if numero % 5==0:
    resposta = "é divisível por 5"

else:
    resposta = "Não é divisível por 5"


print("O número ", resposta)