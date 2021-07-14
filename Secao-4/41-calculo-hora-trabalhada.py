# leia o valor da hora trabalhada e a quantidade de horas trabalhadas e imprima o valor a ser pago adicionando 10%
# sobre o valor calculado

valor_hora = float(input('Digite o valor da hora trabalhada: '))
qtd_horas = float(input('Digite a quantidade de horas trabalhadas: '))
valor_total = valor_hora * qtd_horas
valor_pago = valor_total + (valor_total * 10 / 100)

print(f'O valor a ser pago é de R${valor_pago:.2f}')



