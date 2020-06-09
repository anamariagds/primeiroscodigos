#Entrada de dados

custo_frabrica = float(input("Qual o custo de fábrica: "))

#Processamento de dados

distribuidor = custo_frabrica*0.28
imposto = distribuidor *0.45
consumidor = custo_frabrica + distribuidor + imposto

#Saída de dados

print("O consumidor vai pagar: ",consumidor, "reais")
