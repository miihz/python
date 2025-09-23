def apresentacao(Nome, NomeMae, NomePai):
    print(f"Nome: {Nome}")
    print(f"Nome da mãe: {NomeMae}")
    print(f"Nome do Pai:{NomePai}")

Nome = str(input("digite seu nome completo"))
NomeMae = str(input("digite o nome completo da sua mae"))
NomePai = str(input("digite o nome completo de seu pai"))

print(f"{Nome}, {NomeMae}, {NomePai}")

apresentacao(Nome, NomeMae, NomePai)