# R$780.000,00 serão divididos entre três ganhadores de um concurso. Sendo 46% para o primeiro ganhador,
# 32% para o segundo ganhador e o terceiro ganhador recebe o restante.

premio = 780_000
ganhador1 = premio * 0.46
ganhador2 = premio * 0.32
ganhador3 = premio - (ganhador2 + ganhador1)

print(f'O primeiro ganhador recebeu R${ganhador1}, o segundo ganhador recebeu R${ganhador2} e o terceiro ganhador recebeu R${ganhador3}')