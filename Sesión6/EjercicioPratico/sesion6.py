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
#1. leer un nùmero de 4 dígitos mostrar el dígito mayor e informar si es par o impar
    #num % 10: me devuelve el ultimo dígito    4322 % 10 => 2
    #int(hum/10): elimina el ultimo dígito.
    #hum // 10: elimina el ultimo dígito.
    num = int(input("Digite el numero de 4 dígitos: "))

    digNum1 = num % 10
    digNum2 = (num // 10) % 10
    digNum3 = (num //100) % 10
    digNum4 = (num // 1000) % 10

    if (digNum1 > digNum2 and digNum1 > digNum3 and digNum1 > digNum4 ):
        NumMayor = digNum1
    elif digNum2 > digNum1 and digNum2 > digNum3 and digNum2 > digNum4:
        NumMayor = digNum2
    elif (digNum3 > digNum1 and digNum3 > digNum2 and digNum3 > digNum4):
        NumMayor = digNum3
    else:
        NumMayor = digNum4

    if (NumMayor % 2) == 0:
        siPar= "PAR"
    else:
        siPar= "IMPAR"

    print(f"El dígito mayor es {NumMayor} y es {siPar}.")

 

def funcion2():
    print("Funcion 2.")
    #   2. Leer dos números de 3 dígitos cada uno, formar un tercer número 
    #      con el mayor del primero y el menor del segundo.

    num1 = int(input("Digite el primer numero de 3 dígitos: "))
    num2 = int(input("Digite el segundo numero de 3 dígitos: "))






    #Calculamos el Numero Mayor del primero
    digNum1 = num1 % 10
    digNum2 = (num1 // 10) % 10
    digNum3 = (digNum1 //100) % 10

    numMayor = digNum1

    if numMayor < digNum2:
        numMayor = digNum2
    if numMayor < digNum3:
        numMayor = digNum3

    print("\n")
    print(f"El dígito mayor es {numMayor}")

    #Calculamos el numero  menor del segundo.

    digNum1 = num2 % 10
    digNum2 = (num2 // 10) % 10
    digNum3 = (num2 //100) % 10

    numMenor = digNum1

    if numMenor > digNum2:
        numMenor = digNum2
    if numMenor > digNum3:
        numMenor = digNum3


    print(f"El dígito Menor es {numMenor}")
    print("\n")

    # Formar un tercer número 
    # con el mayor del primero y el menor del segundo.

    newNum = str(numMayor) + str(numMenor)
    print(f"El nuevo numero es {numMayor} + {numMenor} es: {newNum}")

def funcion3():
    print("FUNCIÓN 3.")
    #3. Leer un número de 3 dígitos y formar el mayor número posible 
    #      con sus cifras.
    #Escribe el código de la tercera opción aquí
    #num % 10: extraer el último dígito.
    #int(num/10): elimina el último dígito.
    #num//10: elimina el último dígito.
    #int(num/100): elimina los dos últimos dígitos.
    #int(num/1000): elimina los tres últimos dígitos.


    num = int(input("Digite un número de 3 dígitos: ")) # 852

    d3 = num%10 #  2
    d2 = int(num/10)%10 #  5
    d1 = int(num/100)%10 #  8

    mayor = d3 # 2
    nNum = int(str(d1) + str(d2))  # 85

    if mayor < d2:
        mayor = d2 # 5
        nNum = int(str(d1) + str(d3))  # 82
    if mayor < d1:
        mayor = d1 # 8
        nNum = int(str(d2) + str(d3))  # 52


    d2 = nNum%10 #  2
    d1 = int(nNum/10)%10 #  5

    if d2 < d1:
        nNum = int(str(mayor) + str(d1) + str(d2))
    else:
        nNum = int(str(mayor) + str(d2) + str(d1))

    print(f"El nuevo número formado por {num} es {nNum}.")







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