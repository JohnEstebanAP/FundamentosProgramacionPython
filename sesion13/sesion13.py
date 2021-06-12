"""
Matrices o vectores bidimensionales

En Python podemos trabajar los arreglos bidimensionales como listas de listas, es decir, cada elemento de la lista es una lista.

Nota Existe una librería en Python que maneja tanto vectores como matrices llamada numpy. 
Esta librería está por fuera del alcance de este curso pero puedes investigarla.

Veamos un ejemplo:
"""
def ejemplo1():
    a = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0]]
    print(a)

#ejemplo1()

#O podemos recorrer todos los elementos e imprimir como una matriz
def ejemplo2():
    a = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

#ejemplo2()

#Actividad 1
#
#Vamos a escribir una funcion que llene una matriz de 5 filas y 10 columnas con números enteros entre 1 y 100
#aleatorios, imprima los valores máximo y mínimo y sus posiciones dentro de la matriz.

#actividad1()
import random

def escribirMatriz(n,m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(random.randint(1,100))
        matriz.append(fila)

    return matriz

def leerMatriz(n,m,matriz):
    
    for i in range(n):
        for j in range(m):
            print(matriz[i][j], end = " ")
        print("")

def numMayor(n,m,matriz):
    mayor = matriz[0][0]

    for i in range(n):
        for j in range(m): 
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
                posicion1= i
    #Esto es una prueba, matriz.index(x) nos permite saber 
    # la posición en la que esta un valor x.            
    posicion2 = matriz[posicion1].index(mayor)

    resultado = [posicion1,posicion2,mayor]
    return    resultado       
    
def numMenor(n,m,matriz):
    menor = matriz[0][0]

    for i in range(n):
        for j in range(m): 
            if matriz[i][j] < menor:
                menor = matriz[i][j]
                posicion1= i
    #Esto es una prueba, matriz.index(x) nos permite saber 
    # la posición en la que esta un valor x.            
    posicion2 = matriz[posicion1].index(menor)

    resultado = [posicion1,posicion2,menor]
    return    resultado       
    

def sumarMatriz(n,m,A,B,C):
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append((A[i][j])+(B[i][j]))
        C.append(fila)

    return C

def actividad1():
    matriz = []
    matriz = escribirMatriz(5,10)
    leerMatriz(5,10,matriz)
    mayor = numMayor(5,10,matriz)
    print(" ")
    print(f"El numero mayor es: {mayor[2]}")
    print(f"En la posicion {mayor[0]}, {mayor[1]}")
    menor = numMenor(5,10,matriz)
    print(" ")
    print(f"El numero menor es: {menor[2]}")
    print(f"En la posicion {menor[0]}, {menor[1]}")


#Actividad 2
#
#El producto escalar de un número real, x , y una matriz A es la matriz xA. 
#Cada elemento de la matriz xA es x veces su elemento correspondiente en A.
#
#Diseñemos una funcion escalar(matriz, escalar) que dada matriz[n][m] y un escalar, 
#imprima el producto escalar de la matriz.

def matrizEscalar(n,m,x,matriz):
    matrizB = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append((matriz[i][j])*x)
            
        matrizB.append(fila)

    return matrizB


def actividad2():
    matriz = []
    matriz = escribirMatriz(3,3)
    print("\n")
    print("Matriz A")
    leerMatriz(3,3,matriz)

    print("\n")
    print("Matriz B")
    matrizB = matrizEscalar(3,3,2,matriz)
    leerMatriz(3,3,matrizB)

if __name__ == "__main__":
    #actividad1()
    actividad2()

