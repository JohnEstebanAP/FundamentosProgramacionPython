

# Escribir
nm = input("Digité la cantidad de filas y de columnas [n,m]:  ") # Leer n, m
nm = nm.split(",") # ["3","3"]  nos cra un vector apartir del separador
n= int(nm[0]) # 3
m= int(nm[1]) # 39

matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        fila.append(int(input(f"Digite un valor [{i+1}][{j+1}]: ")))
    matriz.append(fila)

print(matriz)


#LEER
for i in range(n):
    for j in range(m):
        print(matriz[i][j], end = " ")
    print("")