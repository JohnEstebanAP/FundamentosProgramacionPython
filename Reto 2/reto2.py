#John Esteban Alvarez Piedrahita
#Número de identificacion: 1017272663

cantidadP = 0
var_1 = 0.0
var_2 = 0
Salida = ""
genBoleano = False
mAlert1 = 0
mAlert2 = 0
mNOAlert =0

hAlert1 = 0
hAlert2 = 0
hNOAlert =0

#print("Por favor ingrese la candidad de personas: ")
cantidadP = int(input())

for i in range(1,cantidadP+1):
        
    #print("Por Favor ingrese los valores de hemoglobina")
    var_1= float(input())

    genBoleano = False
    while genBoleano == False:
        #print("Por Favor ingrese  el género del paciente (1: Masculino, 2: Femenino)")
        var_2= float(input())
        if var_2 == 1 or var_2 == 2:
            genBoleano = True

    
    if var_2 == 1:
        #Masculino
        #print("el genero es Masculino",var_2)
        if var_1 < 13.2:
            #print("Alerta 1")
            hAlert1 += 1 
        elif var_1 >= 13.2 and var_1 <= 16.6:
            #print("Sin alerta")
            hNOAlert += 1
        elif var_1 > 16.6:
            #print("Alerta 2")
            hAlert2 += 1
    elif var_2 == 2:
        #Femenino
        #print("el genero es Femenino",var_2)
        if var_1 < 11.6:
            #print("Alerta 1")
            mAlert1 += 1
        elif var_1 >= 11.6 and var_1 <= 15:
            #print("Sin alerta")
            mNOAlert += 1
        elif var_1 > 15:
            #print("Alerta 2")
            mAlert2 += 1
    
        #print("No es posible generar la alerta")
print(mAlert1,mAlert2,mNOAlert,hAlert1,hAlert2,hNOAlert)