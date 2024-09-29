# Peça ao usuário para inserir um número flutuante e o número de casas decimais desejado. Use f-strings para formatar o número com o número de casas decimais especificado e exiba o resultado.

numero = float(input("Digite um número flutuante: "))
decimal = int(input("Digite o número de casasa decimais desejado: "))

print(f"O número formatado é: {numero:.{decimal}f}")