n = int(input("Digité la cantidad de posiciones: "))
vector = []

#vector[0] = 3  esta operación no esta permitida
# Escribir un vector
for i in range(0,n,1):
    valor = int(input(f"Digite el valor {i+1}: "))
    vector.append(valor)

# Imprimir o leer un vector
for i in range(0,n,1):       
    print(vector[i])
      
print(vector)