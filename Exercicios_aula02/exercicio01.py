# Descrição: Peça ao usuário para inserir um número e use uma função para calcular e retornar o fatorial desse número. O fatorial de um número não negativo ( n ), denotado por ( n! ), é o produto de todos os números positivos menores ou iguais a ( n ).

numero = int(input("Digite um número: "))

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial

print(f"O fatorial de {numero} é: {calcular_fatorial(numero)}")