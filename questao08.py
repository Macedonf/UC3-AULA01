idade = int(input("Digite sua idade: "))

permissao = input("Você possui permissão dos pais? (sim/não): ").strip().lower()

if idade < 18 and permissao != 'sim':
    print("Você não pode participar da viagem.")
else:
    print("Você pode participar da viagem.")
