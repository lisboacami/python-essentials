# Ler um número de 1000 a 9999 e imprimir um dígito por linha:

num = int(input('Digite um número de 1000 a 9999: '))

while num < 1000 or num > 9999:
    num = int(input('Digite um número de 1000 a 9999: '))

print(str(num)[0])
print(str(num)[1])
print(str(num)[2])
print(str(num)[3])