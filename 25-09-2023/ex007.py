def menor_maior_valor(lista):
    
    maior_valor = 0
    menor_valor = lista[0]

    for valores in lista:
        if valores >= maior_valor:
            maior_valor = valores
        
        if valores < menor_valor:
            menor_valor = valores

    lista_pos = [menor_valor, maior_valor]
    return lista_pos

lista = [40, 30, 4, 10, 100, 9, 20, 10, 3, 10]
print(menor_maior_valor(lista))

# teste