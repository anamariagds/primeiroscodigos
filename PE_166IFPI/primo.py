#Desenvolva um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
p = 0
for c in range(1, n + 1):
    if n % c ==0:
        p += + 1
if p == 2:
    print('PRIMO')
else:
    print('NÃO É PRIMO')
