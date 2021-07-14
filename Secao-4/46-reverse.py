# Faça um programa que leia um número inteiro de três digitos (de 100 a 999)
# Gere outro número formado pelos digitos invertidos do número lido.

num = int(input('Digite um número de 100 a 999: '))

while num < 100 or num > 999:
    num = int(input('Digite um número de 100 a 999: '))

print(str(num)[::-1])







