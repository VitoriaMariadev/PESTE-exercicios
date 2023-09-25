lista = [1, 3, 60, 10, 100, 9, 20, 10, 3, 10]
lista_vazio = []

for valores in lista:
    if valores%2 == 0:
        lista_vazio.append(valores)

print(lista_vazio)