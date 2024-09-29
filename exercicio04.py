#Solicite ao usuário um saldo inicial, a taxa de juros anual e o número de anos. Use um loop while para simular o aumento do saldo com juros compostos ao longo dos anos e imprima o saldo final após o período especificado.

saldo_inicial = float(input("Digite o saldo inicial: "))
juros = float(input("Digite a taxa de juros anual em porcentagem: "))
anos = int(input("Digite o número de anos: "))

taxade_juros = juros / 100
saldo_final = saldo_inicial

ano_atual = 0

while ano_atual < anos:
    saldo_final += saldo_final * taxade_juros
    ano_atual += 1

print(f"O saldo final após {anos} anos será: R${saldo_final:.2f}")
