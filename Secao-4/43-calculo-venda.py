# Programa para auxiliar vendedores. A partir de um valor lido, calcular:
# O total a pagar a vista com desconto de 10%
# O valor de cada parcela, no parcelamento de 3x sem juros
# A comissão do vendedor no caso de a venda ser à vista(5% em cima do valor com desconto)
# A comissão do vendedor no caso de parcelamento(5% sobre o valor total)

valor_venda = float(input('Digite o valor da venda: R$'))
pgto_a_vista = valor_venda - (valor_venda * 10 / 100)
valor_parcela = valor_venda / 3
comissao_a_vista = pgto_a_vista * 5 / 100
comissao_parcelado = valor_venda * 5 / 100

print(f'Valor para pagamento à vista: R${pgto_a_vista:.2f}')
print(f'Valor de cada parcela em 3 vezes sem juros: R${valor_parcela:.2f}')
print(f'Comissão do vendedor(a) caso a venda seja paga à vista: R${comissao_a_vista:.2f}')
print(f'Comissão do vendedor(a) caso a venda seja paga parcelada: R${comissao_parcelado:.2f}')