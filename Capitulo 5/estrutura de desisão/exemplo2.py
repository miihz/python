def quadrado(num):
   if num >= 0:
        return num ** 2
   else:
        return "Número negativo, não é possível calcular o quadrado."

num = float(input("Digite um número:"))
resultado = quadrado(num)
print("Resultado:", resultado)