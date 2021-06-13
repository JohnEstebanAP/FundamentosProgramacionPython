def leerMatriz(f,c,A):
    #LEER
    
    for i in range(f):      #i: 1, n, 1 hacer
        fila = []
        for j in range(c):  #j: 1, m, 1 hacer        
            fila.append(int(input(f"Digite valor [{i+1}][{j+1}]: ")))

        A.append(fila)   

def escribirMatriz(A):
    #ESCRIBIR
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end = " ")

        print()

def sumarMatriz(n,m,A,B,C):   
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(A[i][j] + B[i][j])
        
        C.append(fila)
    

def valorMaximoMatriz(A):
    maximo = A[0][0]
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] > maximo:
                maximo = A[i][j]
                mI, mJ = i, j

    print(f"Valor máximo es {maximo} en la posición A[{mI+1}][{mJ+1}]")

def valorMinimoMatriz(A):
    minimo = A[0][0]
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] < minimo:
                minimo = A[i][j]
                mI, mJ = i, j
            
    print(f"Valor mínimo es {minimo} en la posición A[{mI+1}][{mJ+1}]")

import random
def llenarMatrizNumAleatorios(f,c,A, rIni, rFin):   
    for i in range(f):     
        fila = []
        for j in range(c):      
            fila.append( random.randint(rIni,rFin) )

        A.append(fila) 



def escalar(matriz, escalar):    
    B = []
    for i in range(len(matriz)):     
        fila = []
        for j in range(len(matriz[0])):      
            fila.append( escalar * matriz[i][j] )

        B.append(fila) 
    
    escribirMatriz(B)

def escribirMatrizDiagonalPrincipal(A):
    if len(A) == len(A[0]):
        for i in range(len(A)):
            for j in range(len(A[i])):
                if i == j:
                    print(A[i][j], end = " ")
                else:
                    print(" ", end = " ")
            print()
    else:
        print("La matriz no es cuadrada")


"""
Matrices o vectores bidimensionales

Vamos a utilizar esta sesión para repasar los conceptos vistos y a aprender otras funciones interesantes 
en Python.

La función string.split(), por ejemplo, toma una cadena de caracteres (string) y la pasa a una lista.
Por defecto el separador es cada espacio en blanco, pero se puede seleccionar cualquier separador. 
Veamos un ejemplo:
"""
def ejemplo1(frase):
    lista = frase.split()
    print(lista)



#Actividad 1
#
#Escribe una función actividad1(x, n) que reciba una frase x y un numero entero n 
#e imprima una lista con las palabras cuya longitud sea mayor a n de entrada.

#"Esta es una prueba para pasar a una lista"
#n = 3
def actividad1(x, n):
    lista = x.split() # lista = [ i = "Esta", "es", "una", "prueba", "para", "pasar", "a", "un", "lista"]
    nLista = []
    for i in lista:
        if len(i) > n:
            nLista.append(i)

    return nLista



#Actividad 2
#
#Creemos ahora una función crearMatriz(m,n) que genere una matriz de M * N con números
#  aleatorios entre 0 y 9 
# y la retorne.
#
#Creemos también una función calcularPromedio(T) que dada una matriz T, genere un promedio de todos 
#sus elementos y lo retorne.
#
#Finalmente una función actividad2(m,n) que llame a crearMatriz, pase esa matriz a calcularPromedio(T) 
#y que genere una matriz que tenga el valor 1 en aquellas posiciones donde el valor sea mayor o igual 
#al promedio en T y cero (0) donde el valor de la posición en T sea menor que el promedio.
#
#Imprimir ambas matrices.

def actividad2(m,n):
    
    aM = crearMatriz(m,n)

    print("\nMatriz Aleatoria:")
    escribirMatriz(aM)

    promedio = calcularPromedio(aM)
    print(f"\nEl promedio es igual a {promedio:0.2f}")

    nM = []
    for i in range(m):      #i: 1, n, 1 hacer
        fila = []
        for j in range(n):  #j: 1, m, 1 hacer     
            if aM[i][j] >= promedio:
                fila.append( 1 )
            else:
                fila.append( 0 )

        nM.append(fila)   

    print("\nNueva Matriz:")
    escribirMatriz(nM)




def calcularPromedio(T):    
    cantidad = len(T) * len(T[0])
    acumulador = 0
    for i in range(len(T)):
        for j in range(len(T[0])):
            acumulador += T[i][j]
        
    return acumulador / cantidad



def crearMatriz(m,n):
    A = []
    llenarMatrizNumAleatorios(m,n,A,0,9)

    return A


if __name__ == "__main__":
    #ejemplo1("Esta es una prueba para pasar a una lista")
    #frase = input("Escriba la frase: ")
    #n = int(input("Digite valor de n: "))
    #print(actividad1(frase,n))

    continuar = True
    while continuar:
        nm = input("Digite la cantidad filas y columnas [fxc]: ") # "3 4 5" ---> sprit(",") ---> [ "3", "4" ]    
    
        nm = nm.split("x")

        if len(nm) != 2:
            print("¡Error, debe digitar dos valores!")
        else:
            
            m, n = int(nm[0]), int(nm[1])
    
            actividad2(m,n)
            break

    