# Diseñar 3 opciones:
#
#   1. Leer un número de 4 dígitos, mostrar el dígito mayor e 
#      informar si es par o impar.
#   2. Leer dos números de 3 dígitos cada uno, formar un tercer número 
#      con el mayor del primero y el menor del segundo.
#   3. Leer un número de 3 dígitos y formar el mayor número posible 
#      con sus cifras.
#   
# Luego crea un menú con las tres opciones.

def funcion1():
    #Escribe el código de la primera opción aquí
    print("El mayor dígito es " ) 

def funcion2():
    #Escribe el código de la segunda opción aquí
    print("El nuevo dígito es " )

def funcion3():
    #Escribe el código de la tercera opción aquí
    print("El nuevo dígito es ")


    #Escribe el código aquí para que el usuario seleccione una opción. Llamas cada opción como
op= int(input("Digite su opcion [1-3]: "))

if op == 1:
    funcion1()
elif op == 2:
    funcion2()
elif op == 3:
    funcion3()
else:
    print()