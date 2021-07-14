# encanador recebe 30 reais por dia. Faça um programa que solicite o numero de dias trabalhados pelo encanador
# e imprima a quantia liquida que deverá ser paga, sabendo que são descontados 8% de imposto de renda

valor_diaria = 30
dias_trabalhados = int(input('Digite o total de dias trabalhados:'))
total_bruto = dias_trabalhados * valor_diaria

print(total_bruto)

total_liquido = total_bruto - (total_bruto * 0.08)

print(f'A quantia líquida a ser paga é de R${total_liquido}')

