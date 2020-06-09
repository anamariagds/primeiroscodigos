#Entrada de dados

x1 = int(input("Digite x1: "))
y1 = int(input("Digite y1: "))

x2 = int(input("Digite x2: "))
y2 = int(input("Digite y2: "))

#Processamento de dados

dist = ((x2-x1)**2) + ((y2-y1)**2)

dist = dist**(1/2)

#Saída de dados

print("A distância entre o ponto A(",x1,",",y1,") e o ponto B(",x2,",",y2,") é: ",round(dist,2))
