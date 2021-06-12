
def leerMatriz(n,m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(int(input(f"Digite un valor [{i+1}][{j+1}]: ")))
        matriz.append(fila)

    return matriz

def escribirMatriz(n,m,matriz):
    
    for i in range(n):
        for j in range(m):
            print(matriz[i][j], end = " ")
        print("")

def sumarMatriz(n,m,A,B,C):
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append((A[i][j])+(B[i][j]))
        C.append(fila)

    return C
            



if __name__ == "__main__":
    nm = input("Digité la cantidad de filas y de columnas [n,m]:  ") # Leer n, m
    nm = nm.split(",") # ["3","3"]  nos cra un vector apartir del separador
    n= int(nm[0]) # 3
    m= int(nm[1]) # 39
  
    C = []

    print("Llene la matriz A")
    matrizA = leerMatriz(n,m)
   
    print("Llene la matriz B")
    matrizB = leerMatriz(n,m)
   


    print("Matriz A")
    escribirMatriz(n,m,matrizA)
    
    print("Matriz B")
    escribirMatriz(n,m,matrizB)

    sumarMatriz(n,m,matrizA,matrizB,C)  
    print("Matriz C")
    escribirMatriz(n,m,C)