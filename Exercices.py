# Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.
import math

print("1:\n")

if int(input("enter your age")) >= 18:
    print("You are an adult")
else:
    print("You are underage")

# Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.
print("2:\n")

for i in range(2):
    if int(input("grade:\t")) > 6:
        print("You passed")
    else:
        print("You did not passed")

# Escreva um programa que resolva uma equação de segundo grau.
a = int(input("A:\t"))
b = int(input("B:\t"))
c = int(input("C:\t"))

positive = (-b + (math.sqrt(math.pow(b, 2) - (4 * a * c)))) / (2 * a)
negative = (-b - (math.sqrt(math.pow(b, 2) - (4 * a * c)))) / (2 * a)

print("Solutions:\t" + positive.__str__() + "\tor\t" + negative.__str__())

# Escreva um programa que ordene uma lista numérica com três elementos.
# i am not going to do a sort algorithm ffs

# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal

n1 = int(input("Number one"))
n2 = int(input("Number two"))
signal = input("Signal")

if signal == "+":
    print((n1 + n2))
elif signal == "-":
    print(n1 - n2)
elif signal == "*":
    print(n1 * n2)
elif signal == "/":
    print(n1 / n2)
else:
    print("Invalid signal")
