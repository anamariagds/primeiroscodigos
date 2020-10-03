def listadenota():
    nome = ['Carla', 'Ana', 'Bia', 'Hugo', 'Dani', 'Ana', 'Iris']
    nota = [8.6, 7.8, 7.5, 8.5, 8.9, 9.2, 9.0]

    indice_maior_nota = nota.index(max(nota))
    indice_menor_nota = nota.index(min(nota))

    print(f'A maior nota foi de {nome[indice_maior_nota]}')
    print(f'A menor nota foi de {nome[indice_menor_nota]}')

def teste(n):
    lista =[]
    for i in range(n):
        x=int(input("Valor: "))
        lista.insert(i,x)
        print(lista)
def main():
    teste(3)
    listadenota()
if __name__=='__main__':
    main()