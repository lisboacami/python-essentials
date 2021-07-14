
print("Informe o valor total do premio a receber: ")
premio = float(input())
print("Informe o valor apostado pelo apostador 1: ")
ap1 = float(input())
print("Informe o valor apostado pelo apostador 2: ")
ap2 = float(input())
print("Informe o valor apostado pelo apostador 3")
ap3 = float(input())

a_total = ap1 + ap2 + ap3

pap1 = ap1 / a_total
pap2 = ap2 / a_total
pap3 = ap3 / a_total

val1 = pap1 * premio
val2 = pap2 * premio
val3 = pap3 * premio

print(f"O premio do apostador 1 é: {val1:.2f}")
print(f"O premio do apostador 2 é: {val2:.2f}")
print(f"O premio do apostador 3 é: {val3:.2f}")