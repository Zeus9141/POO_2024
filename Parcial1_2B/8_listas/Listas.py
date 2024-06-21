"""
List (Array)
son colecciones o conjunto de datos/valores bajo 
un mismo nombre, para acceder a los valores se hace
con un indice numerico

Nota: sus valores si son modificables

La lista es una coleccion oredenada y modificable.
Permite miembros duplicados

"""

#Ejemplo 1 crear una lista de numeros e imprimir el  contenido

# numeros=23
# numeros=34
# print(numeros)

numeros=[23,34]
print(numeros)

#Recorrer la lista con ciclo for
for i in numeros:
    print (i)
#Recorrer la lista con ciclo while
tamanio=len(numeros)
print(tamanio)
i=0
while i<=len(numeros)-1:
    print(numeros[i])
    i+=1

#Ejemplo 2 crear una lista de palabras y posteriormente
#buscar la coincidencia  de una palabra

palabras=["naranja","utd","america","azul"]

palabra_buscar=input("ingresa la palabra a buscar: ")

for i in palabras:
    if i==palabra_buscar:
        print(f"Se encontra la palabra buscar en la posicion {palabras.index}")
    else:

