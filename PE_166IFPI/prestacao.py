f = float(input("Informe o valor da fatura em atraso: "))
t = int(input("Quantos dias de atraso: "))
taxa = 5

prestacao = f + (f* (taxa/100) *t)
prestacao = round(prestacao, 2)

print("Valor da sua prestaçao com ", t , "dias de atraso fica: ", prestacao)
