# Receba um salário-base e calcule e imprima o salário a receber. Sabendo-se que esse funcionário tem um gratificação
# de 5% e paga 7% de imposto, quanto o funcionário irá receber?

salario_base = float(input('Digite seu salário-base: R$'))
bonus = salario_base + (salario_base * 5 / 100)
imposto = salario_base - (salario_base * 7 / 100)
salario_recebido = salario_base + bonus - imposto

print((f'O total recebido será de R${salario_recebido:.2f}'))

