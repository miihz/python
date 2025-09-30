#faça um programa que receba a idade do usuario e verifique se a idade maior ou igual a 18 anos. Apresente uma mensagem caso ele seja
def verificar_idade(idade):
    if idade >=18:
        return "voce é maior de idade"
    else:
        return "voce não é de maior "

idade = int(input("Digite sua idade: "))

resultado = verificar_idade(idade)

print(resultado)