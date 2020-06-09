#Entrada de dados

saque = int(input("Valor do saque desejado: "))

#Processamento de dados

n1 = saque // 100
resto = saque % 100
n2 = resto // 50 
resto = resto % 50
n3 = resto // 20 
resto = resto % 20
n4 = resto // 10
resto = resto % 10
n5 = resto // 5
resto = resto % 5
n6 = resto // 2

#Saída de dados

print(n1, "notas de R$100")
print(n2,"notas de R$50")
print(n3, "notas de R$20")
print(n4,"notas de R$10")
print(n5,"notas de R$5")
print(n6,"notas de R$2" )

