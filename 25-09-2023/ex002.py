def maior_valor(lista):
    maior_valor = 0
    for valores in lista:
        if valores >= maior_valor:
            maior_valor = valores
    
    return maior_valor

lista = [1, 3, 60, 10, 100, 9, 20]
print(maior_valor(lista))