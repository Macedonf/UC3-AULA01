idade = int(input("Digite sua idade: "))


if idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 64:
    print("Adulto")
else:
    print("Idoso")
