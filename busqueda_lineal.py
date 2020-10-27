import random

def busqueda_lineal(lista, buscar):
    match = False

    for elemento in lista: 
        if elemento == buscar:
            match = True
            break

    return match

if __name__ == '__main__':
    tamano_de_lista = int(input('Ingresa el tamaño de la lista: '))
    objetivo = int(input('Numero a buscar en la lista: '))

    lista = [random.randint(0,100) for i in range(tamano_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El element {objetivo} {"esta" if encontrado else "no esta"} en la lista')