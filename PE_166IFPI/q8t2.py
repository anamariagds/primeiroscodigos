print("Informe 0 se nao hover moedas de algum valor.")

t1 = int(input("Moedas de 1 centavo: "))
t2 = int(input("Moedas de 5 centavos: "))
t3 = int(input("Moedas de 10 centavos: "))
t4 = int(input("Moedas de 25 centavos: "))
t5 = int(input("Moedas de 50 centavos: "))
t6 = int(input("Moedas de 1 real: "))

d = (t1*0.01)+(t2*0.05)+(t3*0.1)+(t4*0.25)+(t5*0.5)+(t6*1)


print("Pedrinho economizou", d, "reais ")
