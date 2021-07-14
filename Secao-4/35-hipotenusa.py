# Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação:
# hipotenusa = a ** 2 + b ** 2 ** (1/2)

import math

a = float(input(f'O valor de um cateto é: '))
b = float(input(f'O valor do segundo cateto é: '))

hipotenusa = math.sqrt((a**2)+(b**2))

print(hipotenusa)