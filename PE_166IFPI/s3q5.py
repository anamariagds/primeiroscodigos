#Entrada de dados

valor = int(input("Valor do produto: "))

#Processamento de dados

prestacao = valor // 3
entrada = (prestacao)+(valor % 3)

#saída de dados

print("Pague uma entrade de:", entrada,"reais, mais duas parcelas de: ", prestacao, "reais")
