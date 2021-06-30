
#John Esteban Álvarez Piedrahita
#Número de identificación: 1017272663

# Código para generar las alertas
def generarAlertas(fila,vectorResultado):

    vectorAlertas = [] # vector para almacenar las alertas
        
    #ciclo para recorrer las filas y realisar al operación
    for i in range(fila):
    
        genero= vectorResultado[0][i]
        emoglovina= vectorResultado[1][i]
       
        if genero == 1:
            #Masculino
            #print("el genero es Masculino",emoglovina)
            if emoglovina < 13.2:
                vectorAlertas.append("Alerta 1")
            elif emoglovina >= 13.2 and emoglovina <= 16.6:
                vectorAlertas.append("Sin alerta")
            elif emoglovina > 16.6:
                vectorAlertas.append("Alerta 2")
        elif genero == 2:
            #Femenino
            #print("el genero es Femenino",emoglovina)
            if emoglovina < 11.6:
                vectorAlertas.append("Alerta 1")
            elif emoglovina >= 11.6 and emoglovina <= 15:
                vectorAlertas.append("Sin alerta")
            elif emoglovina > 15:
                vectorAlertas.append("Alerta 2")
            
    vectorResultado.append(vectorAlertas)
    return vectorResultado



# LLenamos la matriz con los valores corespondientes
def valoresMatriz(canfila):
    matriz = []
    for i in range(canfila):
        fila = []
        #print("Ingrese los balores de cada Paciente")
        valores= (input())
        fila =valores.split()
        matriz.append(fila)
    return matriz

# creamos una función leerGenero para poder determinar la cantidad de mujeres y hombres
def leerGenero(canfila,matriz):
    generoM= 0
    generoF= 0
    for i in range(canfila):
        if int(matriz[i][0]) == 1:
            generoM += 1
        elif int(matriz[i][0]) == 2:
            generoF += 1

    generos = [generoM,generoF]

    return generos

 

#Convertimos toda la matris a float ya que esta en string
def convertiMatrizFloat(canfila,matriz):
    matriz2= []
    for i in range(canfila):
        fila = []
        for j in range(len(matriz[i])):
            fila.append(float(matriz[i][j])) 
        matriz2.append(fila)
    return matriz2

# funcion para poder calcular el promedio de la emoglobina para 
def calcularPromedioHemoglobina(canfila,matriz):
    promedio = 0
    vectorPromedio = []
    for i in range(canfila):
        suma = 0
        for j in range(1,len(matriz[i])):
            suma = suma + matriz[i][j] 

        promedio = suma/ (len(matriz[i])-1) 
        vectorPromedio.append(promedio)

    #ciclo y vector parar poder determinar el genero y poder guadarlo en un vector
    vectorGenero = []
    for i in range(canfila):
        vectorGenero.append(int(matriz[i][0]))
    
    #a vector resultados le asinamos los que seria los resultados de los vetores genero y promedio
    vectorResultados = [vectorGenero,vectorPromedio]
    return(vectorResultados)


#Calculamos el promedio Mayor
def promedioMayor(matrizResultado2):
    indice = 0
    mayor = matrizResultado2[1][0]
    vectMayor = []
    for i in range(len(matrizResultado2[1])):
        if matrizResultado2[1][i] > mayor:
            mayor = matrizResultado2[1][i]
            indice = i

    vectMayor = [indice,mayor]
    return vectMayor

#Calculamos el promedió menor
def promedioMenor(matrizResultado2):

    indice = 0
    menor = matrizResultado2[1][0]
    vectMenor = []
    for i in range(len(matrizResultado2[1])):
        if matrizResultado2[1][i] < menor:
            menor = matrizResultado2[1][i]
            indice = i

    vectMenor = [indice,menor]
 
    return vectMenor

#Creamos un vector con todos los resultados el, genero, el promedio de emoglovina mayor y su  respectiva alerta
def vectorMayor(mayorPro, cantidadP, matriz):
    vect= []
    vect.append(matriz[0][mayorPro[0]])
    vect.append(matriz[1][mayorPro[0]])
    vect.append(matriz[2][mayorPro[0]])

    return vect

#Creamos un vector con tododos los resultados el, genero, el promedio de emoglovina mayor y su  respectiva alerta
def vectorMenor(mayorPro, cantidadP, matriz):
    vect= []
    vect.append(matriz[0][mayorPro[0]])
    vect.append(matriz[1][mayorPro[0]])
    vect.append(matriz[2][mayorPro[0]])

    return vect

# función para imprimir los resultados
def imprimirResultados(VectorMayor, VectorMenor, generoMF):
    print(f"{VectorMayor[0]} {VectorMayor[1]:.2f} {VectorMayor[2]}")
    print(f"{VectorMenor[0]} {VectorMenor[1]:.2f} {VectorMenor[2]}")
    print(f"{generoMF[0]} {generoMF[1]}")


#Función principal donde ejecutamos todo el código
def principal():
    cantidadP = 0

    #print("Por favor ingrese la candidad de personas: ")
    cantidadP = int(input())
    matriz= valoresMatriz(cantidadP)
    matrizFloat = convertiMatrizFloat(cantidadP,matriz)

    generoMF = leerGenero(cantidadP,matriz)
    matrizResultado = calcularPromedioHemoglobina(cantidadP,matrizFloat)
    matrizResultado2 = generarAlertas(cantidadP,matrizResultado)


    mayorPro= promedioMayor(matrizResultado2)
    menorPro= promedioMenor(matrizResultado2)

    VectorMayor = vectorMayor(mayorPro, cantidadP, matrizResultado2)
    VectorMenor = vectorMenor(menorPro, cantidadP, matrizResultado2)

    imprimirResultados(VectorMayor, VectorMenor, generoMF)


if __name__ == "__main__":
    principal() # ejecutamos la función principal








