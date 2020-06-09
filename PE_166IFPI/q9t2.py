print("Mediremos o predio usando semelhança de triangulos")

h = float(input("Informe sua altura: "))
s1 = float(input("Tamanho da sua sombra: "))
s2 = float(input("Sombra do predio: "))

H = (s2/s1)*h

print("A altura do predio e: ", round(H,2), "metros")
