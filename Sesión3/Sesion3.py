# Fundamentos de Programación con Python

## Condicionales

### Si-Sino
### Recuerda que los condicionales nos permiten decidir qué instrucciones ejecutar y cuales no. 

x = int(input("Por favor ingresa un número: "))
if x<0:
    print('X es Negativo')
else:
    print('X es Positivo')

print('Esto ya está por fuera del condicional') #Esta fuera porque ya no hay fabulación

a = int(input("Por favor ingresa un número: "))
b = int(input("Por favor ingresa un número: "))

if a > 2:
    print(a)

if b < 4:
    print(a)


#Actividad 2

#Para ingresar al programa de medicina, 
# el estudiante debe tener diploma de bachiller y 
# ser mayor de 17 años. Creemos el código para 
# validar esta información dadas las variables
#  tieneDiploma (Y/N) y edad (entero).

tieneDiploma = input("ingrese por favor si tiene diploma (Y/N): ")
if tieneDiploma == "y" or tieneDiploma == "Y":
    edad = int(input("Ingrese su edad: "))
    if edad > 17:
        print ("felicidades puede ingresar al programa de medicina.")
    else :
        print(":( no puede ingresar al programa de medicina")
else:
    print("No tiene diploma y no puede ingresar al programa de medicina. ")


#Actividad 3
#Escribe el código para leer un número entero e 
# imprime SI si el último dígito es 4.

numEntero = int(input("Ingrese por favor un numero entero: "))
digito4 = numEntero % 10 

print("el ultimo numero es, ", digito4)
if  digito4 == 4:
    print("El ultimo dígito es 4.")
else:
    print("El ultimo dígito No es 4.")