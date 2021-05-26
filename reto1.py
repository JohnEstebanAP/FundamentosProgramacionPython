#John Esteban Alvarez Piedrahita
#Número de identificacion: 1017272663

var_1 = 0.0
var_2 = 0
Salida = ""
#print("Por Favor ingrese los valores de hemoglobina")
var_1= float(input())
#print("Por Favor ingrese  el género del paciente (1: Masculino, 2: Femenino)")
var_2= float(input())
if var_2 == 1:
  #Masculino
  #print("el genero es Masculino",var_2)
  if var_1 < 13.2:
     print("Alerta 1")
  elif var_1 >= 13.2 and var_1 <= 16.6:
     print("Sin alerta")
  elif var_1 > 16.6:
     print("Alerta 2")
elif var_2 == 2:
  #Femenino
  #print("el genero es Femenino",var_2)
  if var_1 < 11.6:
     print("Alerta 1")
  elif var_1 >= 11.6 and var_1 <= 15:
     print("Sin alerta")
  elif var_1 > 15:
     print("Alerta 2")
else:
  print("No es posible generar la alerta")
