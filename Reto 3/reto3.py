#John Esteban Alvarez Piedrahita
#Número de identificacion: 1017272663


#esta función nos ayuda a determinar la alerta del promedio de la hemoglobina de los hombres
def alertaM(hemoglobina):
    #Masculino
    #print("el genero es Masculino",genero)
    if hemoglobina < 13.2:
        alerta = "Alerta 1"

    elif hemoglobina >= 13.2 and hemoglobina <= 16.6:
        alerta ="Sin alerta"

    elif hemoglobina > 16.6:
        alerta = "Alerta 2"
    return alerta        


#Esta función nos ayuda a determinar la alerta del promedio de la hemoglobina de las mujeres
def alertaF(hemoglobina):
    #Femenino
    #print("el genero es Femenino",genero)
    if hemoglobina < 11.6:
     
        alerta = "Alerta 1"
    elif hemoglobina >= 11.6 and hemoglobina <= 15:
        #print("Sin alerta")
        alerta ="Sin alerta"
        
    elif hemoglobina > 15:
        #print("Alerta 2")
        alerta = "Alerta 2"
    return alerta    



#print("Por favor ingrese la candidad de personas: ")
cantidadP = int(input())

vectorM = []# vector para almacenar la hemoglobina de los hombres
vectorF = []# vector para almacenar la hemoglobina de las mujeres


#primer siclo para guradar los datos de los x pacientes
for i in range(1,cantidadP+1):
        
    #El siclo while se repite infinitamente asta que se ingrese un válor correcto para el genero hombre o mujer[1,2]
    genBoleano = False
    while genBoleano == False:
       
        valores= (input())
        fila =valores.split()
        hemoglobina = float(fila[0])
        genero = int(fila[1])

        if genero == 1 or genero == 2:
            genBoleano = True

    # condicional if para determinar si es hombre o mujer y almacenar los valores en un vector

    if genero == 1:
        #Masculino
        #print("el genero es Masculino",genero)
            vectorM.append(hemoglobina)
    elif genero == 2:
        #Femenino
        #print("el genero es Femenino",genero)
            vectorF.append(hemoglobina)



# calculo promedio de la hemoglobina tanto pra hombre como mujeres
promedioM = sum(vectorM) / len(vectorM)
promedioF = sum(vectorF) / len(vectorF)

promedioMayorM = 0
promedioMenorM = 0
promedioIgualM = 0

promedioMayorF = 0
promedioMenorF = 0
promedioIgualF = 0

# Calculo numero de hombres que tienen su hemoglobina superior, inferior o igual a el promedio
for i in range(len(vectorM)):
    if vectorM[i] > promedioM:
        promedioMayorM += 1
    elif vectorM[i] < promedioM:
        promedioMenorM += 1
    elif vectorM[i] == promedioM:
        promedioIgualM += 1

# Calculo numero de mujeres que tienen su hemoglobina superior, inferior o igual a el promedio
for i in range(len(vectorF)):
    if vectorF[i] > promedioF:
        promedioMayorF += 1
    elif vectorF[i] < promedioF:
        promedioMenorF += 1
    elif vectorF[i] == promedioF:
        promedioIgualF += 1


# determino el tipo d alertá para cada promedio
alertaM = alertaM(promedioM)
alertaF = alertaF(promedioF)

#Imprimimos los resultados
print(f"{promedioM:.2f} {alertaM}")
print(f"{promedioF:.2f} {alertaF}")
print(f"{promedioMayorM} {promedioMayorF}")
print(f"{promedioMenorM} {promedioMenorF}")
print(f"{promedioIgualM} {promedioIgualF}")