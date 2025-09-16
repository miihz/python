def valideLogin(nome, senha):
    if (nome == "Emilly" and senha == "senha321"):
        return print("Seja bem vindo", nome, senha)
    else:
        return print("Senha ou Login invalido")

print("=== Digite su nome ===")
nome = input()
print("=== Digite sua senha ===")
senha = input()

valideLogin(nome, senha)