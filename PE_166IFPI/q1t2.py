print("Controle de vendas padaria Hotpao")

p = int(input("Quantos paes foram vendidos hoje: "))
b = int(input("Quantas broas foram vendidas hoje: "))

vendas = (p*0.12) + (b*1.50)
guardar =round( vendas*0.1, 2)

print("Hoje arrecadou: ", vendas, "reais Guarde: ", guardar, "reais na poupança" )
