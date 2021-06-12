"""
Matrices o vectores bidimensionales

Vamos a continuar con el trabajo de matrices usando lista de listas. 
Como vimos en la sesión anterior, las operaciones de este tipo de matrices se pueden realizar con ciclos anidados.
"""

#Actividad 1

#Escribe una función actividad1(x) que imprima la diagonal principal de una matriz x. 
#Asegúrate de validar si la matriz es cuadrada, sino devuelve un mensaje, "La matriz no es cuadrada"

 
#actividad1([[1,1],[2,7,2],[3,3,3]])
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
        print()

def diagonalPrincipal(n,m,matriz):   
    for i in range(n):
        for j in range(m):
            if i == j:
                print(matriz[i][j], end = " ")
            else:
                print(" ", end = " ")
        print()


def actividad1():
    n= int(input("Digité por favor la cantidad de filas de la matriz: "))
    m= int(input("Digité por favor la cantidad de columnas de la matriz: "))
    matriz = escribirMatriz(n,m)

    print("La MAtriz generada es: ")
    leerMatriz(n,m,matriz)

    if len(matriz) == len(matriz[0]):
        print("La matriz si es cuadrada")
        diagonalPrincipal(n,m,matriz)
    else: 
        print("La matriz no es Cuadrada")
    
#Actividad 2
#
#Creemos ahora una función actividad2() que reciba los elementos de una matriz 3x3 e imprima:
#
#   - La primera fila
#   - La primera columna
#   - Accede al elemento en la fila 1, columna 1.
#
#Los valores son ingresados por filas [0][1], [0][2], [0][3], [1][0], etc


#actividad2()
def actividad2():
    
    matriz = escribirMatriz(3,3)
    print("La MAtriz generada es: ")
    leerMatriz(3,3,matriz)

    print(f"La Primera filan y La Primera Columna es: ")
    imprimirFila1(matriz)
    imprimirColumna1(matriz)

    print(f"El elemento en la fila 1 columna 1 es: {matriz[0][0]}")


def imprimirFila1(matriz):
    for i in range(3):
        print(matriz[0][i], end = " ")
    print()

def imprimirColumna1(matriz):
    for i in range(1,3):
        print(matriz[i][0])



if __name__ == "__main__":
    #actividad1()
    actividad2()
