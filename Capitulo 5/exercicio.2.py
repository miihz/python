def resultadoFinal(numSomados,valentia):
    return (f"Somando todos os valores e subtraindo por 10 o resultado é { numSomados - valentia}")


num1 = int(input("digite um numero inteiro"))
num2 = int(input("digite outro numero inteiro"))
num3 = int(input("digite mais um numero inteiro"))
num4 = int(input("digite o último numero inteiro"))

numSomados = (num1 + num2 + num3 + num4)
valentia = 10

resultadoFinal(numSomados, valentia)