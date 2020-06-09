raio = float(input("Informe o raio da circunferencia: "))
h = float(input("Qual a altura da lata? "))
PI = 3.14159

volume = PI*((raio/2)*h)
volume = round(volume, 2)

print("O vlume dessa lata de oleo eh: ", volume)
