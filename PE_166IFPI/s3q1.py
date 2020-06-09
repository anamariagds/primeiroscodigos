#Entrada de dados

anos = int(input("Quantos anos fumando?\n"))
cig_dia = int(input("Quantos cigarros por dia?\n"))
carteira = float(input("Preço da carteira de cigarro: "))

#Processamento de dados

unidade_cig = (carteira/20)
custo = (anos*365)*cig_dia*unidade_cig

#Saida de dados

print("Em",anos, "anos você gastou", custo,"reais fumando")
