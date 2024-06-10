#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

def mostrar_lista(lista):
    print("Lista de números:")
    for numero in lista:
        print(numero, end=" ")
    print()

def lista_a_string(lista):
    return ' '.join(map(str, lista))

def buscar_elemento(lista, elemento):
    if elemento in lista:
        return f"El elemento {elemento} está en la lista."
    else:
        return f"El elemento {elemento} no está en la lista."

# Lista de números
numeros = [5, 3, 8, 2, 7, 1, 4, 6]

# a. Mostrar la lista
mostrar_lista(numeros)

# b. Convertir la lista a string
lista_string = lista_a_string(numeros)
print("Lista como string:", lista_string)

# c. Ordenar y mostrar la lista
numeros.sort()
mostrar_lista(numeros)

# d. Mostrar longitud de la lista
print("Longitud de la lista:", len(numeros))

# e. Buscar un elemento
elemento_buscado = int(input("Ingrese un número para buscar en la lista: "))
print(buscar_elemento(numeros, elemento_buscado))