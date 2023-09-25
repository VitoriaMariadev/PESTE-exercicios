lista = [1, 3, 60, 10, 100, 9, 20, 10, 3, 10]

num = int(input('Informe um valor: '))

if not num in lista:
    print('Esse valor não está na lista.')

for index in range(len(lista)):
    if num == lista[index]:
        lista[index] = 0
    
print(lista)