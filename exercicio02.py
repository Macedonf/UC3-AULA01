#: Use um loop ‘for’ para iterar de 2 até um número ( N ) fornecido pelo usuário e dentro do loop, use outro loop para verificar se o número atual é primo. Imprima cada número primo encontrado.

n = int(input("Digite um número: "))

for num in range(2, n + 1):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num, end=" ")
        print("É primo")
