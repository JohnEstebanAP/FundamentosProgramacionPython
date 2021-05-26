#Instrucciones, Variables, y Operaciones Matemáticas

#Comencemos por lo más sencillo... 
# Recuerda que programar significa 
# darle instrucciones al computador 
# para que haga lo que yo quiera. 
# Podemos comenzar por pedirle que 
# imprima algo para nosotros:

print("¡Hola soy john!")
print("\n")


# Para asignarle un valor a una variable lo reslisamos asi: {valor_uno=1}
# python es de tipado devil por lo qe no tenemos que indicar si es de tipo 
# int, fload, string, buleano, etc

valor_uno = 5
valor_dos = 8
total = valor_uno + valor_dos
print (f"la suma del numero: {valor_uno} + {valor_dos} es: {total}") # con f"{}" podemor imprimir las variables o concatenar la variables conjunto el texto


#Y si quisieramos leer el valor? 
# Python cuenta con la función 
# input() para leer valores. 
# Vamos a ver como usarla
print("\n")
valor_uno = int(input("digita un numero: ")) # de esta manera tanbien podemos imprimir a la hora de solicitar un valor
valor_dos = int(input("digita un numero: ")) # con int(input()) pasamos el valor que resibimos de tipo testo a un entero
total = valor_uno + valor_dos
print (f"la suma del numero: {valor_uno} + {valor_dos} es: {total}") # con f"{}" podemor imprimir las variables o concatenar la variables conjunto el texto
print("\n")
'''

print("\n")
print("División real")
print("división real ente 6 / 2: ",6/2)
print("división real ente 5 / 2: ",5/2)
print("\n")
print("Division con redondeo")
print("Division con redondeo ente 6 // 2: ",6//2)
print("Division con redondeo ente 5 // 2: ",5//2)
print("\n")
'''

#Actividad 3
#El área de un cuadrado puede 
# calcularse como a^2. 
# Escribe el código para 
# calcular e imprimir el área del cuadrado 

print("Por favor ingrese el lado del cuadrado en metros para calcual la Area")
area = float(input("Area: "))
area = area**2 
print("El area del cuadrado es de:", area, "metros cuadrados")