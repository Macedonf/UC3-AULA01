#Crie uma função que receba uma lista de números e retorne a soma de todos os números.



def soma_lista(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

# Exemplo de uso
numeros = [1, 2, 3, 4, 5]
resultado = soma_lista(numeros)
print(resultado)






def soma_lista(numeros):
    return sum(numeros)
print(soma_lista({1,2,3,4,5}))