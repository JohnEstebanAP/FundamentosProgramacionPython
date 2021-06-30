#John Esteban Álvarez Piedrahita
#Número de identificación: 1017272663

from io import open
#Importo las librerías necesarias para poder trabajar con los archivos.

#Función pra Lectura de el archivo y convertirlo a matriz
def leerMatrizData():
    matrizData = []
    data = open("data.csv","r")
    lista = data.readlines()
    
    for linea in lista:
        fila =  linea.rstrip("\n").split(",")
        #fila[3] = fila[3].rstrip("\n")
        matrizData.append(fila)
    data.close()

    return matrizData


def leerMatriz(A):
    #ESCRIBIR
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f"{A[i][j]}", end = " ")

    print()

# función para poder calcular el promedio de la hemoglobina para 
def calcularPromedioHemoglobina(matriz):
    promedio = 0
    vectorPromedio = []
    vectorGenero = []
    vectorSede = []
    for i in range(1,len(matriz)):
        suma = 0
        for j in range(4,len(matriz[i])):
            suma = suma + float(matriz[i][j]) 

        promedio = suma/ (len(matriz[i])-4) 

        vectorPromedio.append(promedio)
        # guardamos en un vector la sede de cada paciente
        vectorSede.append(int(matriz[i][3]))
        #ciclo y vector parar poder determinar el genero y poder guadarlo en un vector
        vectorGenero.append((matriz[i][1]))
    
    #a vector resultados le asinamos los que seria los resultados de los vetores genero y promedio
    vectorResultados = [vectorSede,vectorGenero,vectorPromedio]
    return(vectorResultados)




# Código para generar las alertas
def generarAlertas(vectorResultado):

    vectorAlertas = [] # vector para almacenar las alertas
        
    #ciclo para recorrer las filas y realisar al operación
    for i in range(len(vectorResultado[1])):
    
        genero = vectorResultado[1][i]
        emoglovina = vectorResultado[2][i]
       
        if genero == "M" or genero == "m":
            #Masculino
            #print("el genero es Masculino",emoglovina)
            if emoglovina < 13.2:
                vectorAlertas.append("Alerta 1")
            elif emoglovina >= 13.2 and emoglovina <= 16.6:
                vectorAlertas.append("Sin alerta")
            elif emoglovina > 16.6:
                vectorAlertas.append("Alerta 2")
        elif genero == "F" or genero == "f":
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

# función para recibir los datos de la sede x y la hemoglobina y
def sedeHemoglobina():
    datosBuscar = []
    print("Ingrese los balores de la sede y la hemoglobina")
    valores= (input())
    fila =valores.split()

    datosBuscar.append(int(fila[0]))
    datosBuscar.append(float(fila[1]))
    return datosBuscar


#Calculamos el promedio Mayor
def promedioMayorPorSede(datosSedeHemoglobina,vectorResultado):
    mayor = 0

    for i in range(len(vectorResultado[2])):
        
        if datosSedeHemoglobina[0] == vectorResultado[0][i]:
            if vectorResultado[2][i] > mayor:
                mayor = vectorResultado[2][i]
                indice = i
    return indice


#Calculamos el promedio Menor
def promedioMenorPorSede(datosSedeHemoglobina,vectorResultado):

    for i in range(len(vectorResultado[2])):
        if datosSedeHemoglobina[0] == vectorResultado[0][i]:
            menor = vectorResultado[2][i]
            break


    for i in range(len(vectorResultado[2])):
        
        if datosSedeHemoglobina[0] == vectorResultado[0][i]:
            if vectorResultado[2][i] < menor:
                menor = vectorResultado[2][i]
                indice = i
    return indice

#¿Cuántos pacientes se encuentran por encima del nivel de hemoglobina Y?
def personasMayorH(datosSedeHemoglobina,vectorResultado):
    mayor = 0
    for i in range(len(vectorResultado[2])):
        if vectorResultado[2][i] > datosSedeHemoglobina[1]  :
                mayor += 1
    return mayor

#¿Cuántos pacientes se encuentran por debajo del nivel de hemoglobina Y?
def personasMenorH(datosSedeHemoglobina,vectorResultado):
    menor = 0
    for i in range(len(vectorResultado[2])):
        if vectorResultado[2][i] < datosSedeHemoglobina[1]  :
                menor += 1
    return menor

#Cuántos pacientes igualan el nivel de hemoglobina Y?
def personasIgualH(datosSedeHemoglobina,vectorResultado):
    igualan = 0
    for i in range(len(vectorResultado[2])):
        if vectorResultado[2][i] == datosSedeHemoglobina[1]  :
                igualan += 1
    return igualan

#Cuántos hombres y cuantas mujeres se encuentran dentro del estudio?
#Creamos una función leerGenero para poder determinar la cantidad de mujeres y hombres
def cantidadGenero(vectorResultado):
    generoM= 0
    generoF= 0
    for i in range(len(vectorResultado[1])):
        if vectorResultado[1][i] == "M" or vectorResultado[1][i] == "m":
            generoM += 1
        elif vectorResultado[1][i] == "F" or vectorResultado[1][i] == "F":
            generoF += 1

    return [generoM,generoF]

# función para calcular sede mayor
def sedeMayor(vectorResultado):
    mayor = 0
    for i in range(len(vectorResultado[0])):
        if vectorResultado[0][i] > mayor:
            mayor = vectorResultado[0][i]
    return mayor

#¿Cuántos pacientes hay registrados en cada sede?
def pacientesPorSede(vectorResultado):
    vectorPacientesPorSede = []
    vectorIndice = []
    vectorCantidad = []
    sedemayor = sedeMayor(vectorResultado)
    indice = 0
    for i in range(sedemayor+1):
        cantidad = 0
        bandera = False
        for j in range (len(vectorResultado[0])):
            if i == vectorResultado[0][j]:
                indice = i
                cantidad += 1
                bandera = True
        if bandera:
            vectorIndice.append(indice)
            vectorCantidad.append(cantidad)

    vectorPacientesPorSede.append(vectorIndice)
    vectorPacientesPorSede.append(vectorCantidad)
    return vectorPacientesPorSede


def imprimirResultados(matrizData, vectorResultado, sedeMayor, sedeMenor, vectorMaMeIg, cantidadPorGenero,pacientesPorSede):
    #nombre,genero,cedula y alerta del paciente
    print(f"{matrizData[sedeMayor+1][0]} {matrizData[sedeMayor+1][1]} {matrizData[sedeMayor+1][2]} {vectorResultado[3][sedeMayor]}")
    print(f"{matrizData[sedeMenor+1][0]} {matrizData[sedeMenor+1][1]} {matrizData[sedeMenor+1][2]} {vectorResultado[3][sedeMenor]}")
    print(f"{vectorMaMeIg[0]} {vectorMaMeIg[1]} {vectorMaMeIg[2]}")
    print(f"M {cantidadPorGenero[0]}")
    print(f"F {cantidadPorGenero[1]}")

    #Creamos un ciclo para imprimir la cantidad de pacientes por sede
    for i in range(len(pacientesPorSede[0])):
        print(f"{pacientesPorSede[0][i]} {pacientesPorSede[1][i]}")
    

# función principal para ejecutar todas las operaciones
def principal():
    while True:
        try:
            matrizData = leerMatrizData()
            vectorPromedioGenero = calcularPromedioHemoglobina(matrizData)
            vectorResultado = generarAlertas(vectorPromedioGenero)
            datosSedeHemoglobina = sedeHemoglobina()
            sedeMayor = promedioMayorPorSede(datosSedeHemoglobina,vectorResultado)
            sedeMenor = promedioMenorPorSede(datosSedeHemoglobina,vectorResultado)
            vectorMaMeIg = [personasMayorH(datosSedeHemoglobina,vectorResultado),personasMenorH(datosSedeHemoglobina,vectorResultado),personasIgualH(datosSedeHemoglobina,vectorResultado)]
            cantidadPorGenero = cantidadGenero(vectorResultado)
            pacientesporSede = pacientesPorSede(vectorResultado)
            imprimirResultados(matrizData, vectorResultado, sedeMayor, sedeMenor, vectorMaMeIg,cantidadPorGenero,pacientesporSede)
            break
        except : 
            principal() # ejecutamos la función principal
            break

if __name__ == "__main__":
    principal() # ejecutamos la función principal