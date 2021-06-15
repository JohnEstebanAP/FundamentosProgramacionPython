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
            print(f"{A[i][j]}", end = " ")

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



def calcularPromedio(T):    
    cantidad = len(T) * len(T[0])
    acumulador = 0
    for i in range(len(T)):
        for j in range(len(T[0])):
            acumulador += T[i][j]
        
    return acumulador / cantidad

