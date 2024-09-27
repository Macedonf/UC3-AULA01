nota = float(input("Digite a nota final do aluno: "))

if nota >= 90:
    print("Excelente")
elif 75 <= nota < 90:
    print("Bom")
elif 50 <= nota < 75:
    print("Satisfatório")
else:
    print("Insuficiente")
