# condicionales y uso basico de las funciones
#Cada ejemplo y actividad será definida como un bloque independiente.
#Si-Sino
#Recuerda que los condicionales múltiples y anidados nos permiten evaluar múltiples casos. 

def actividad1():
    #Escribe el código que imprima un comando dada la luz del semáforo
        #Verde = Siga
        #Amarillo = Precaución
        #Rojo = Pare

    color = input("Digite el color [Verde/ Amarillo/ Rojo] del semaforo: ")
    if color ==  "verde" or color == "Verde" or color == "VERDE":
        return ("siga")
    elif color == "amarillo" or color == "Amarillo" or color == "AMARILLO":
        return("Precaución")
    elif color == "rojo" or color == "Rojo" or color == "ROJO":
        return("Pare")
    else:
        return("Opción incorrecta")



def actividad2():
    #Escribe el código que basado en la actividad 1 y una variable que nos indica si hay peaton o no (hayPeaton), imprima:
        #Verde -------- Si hay peaton - Pare, Sino - Siga
        #Amarillo ----------- Si hay peaton - Pare, Sino - Precaución
        #Rojo = Pare

    hayPeaton = input("por favor ingrese [Y/N] si hay un peaton al frente: ")

    if (hayPeaton == "y" or hayPeaton == "Y"):
        semaforo= actividad1()
        if (semaforo == "siga"):
            print("Si hay peaton - Pare")
        elif semaforo ==  "Precaución":
            print("Si hay peaton - Pare")
        elif semaforo == "Pare":
            print(semaforo) # pare
        else: 
            print(semaforo) # Opción incorrecta
    elif (hayPeaton == "n" or hayPeaton == "N"):
        semaforo= actividad1()
        if (semaforo == "siga"):
            print(semaforo)
        elif semaforo ==  "Precaución":
            print(semaforo)
        elif semaforo == "Pare":
            print(semaforo) # pare
        else: 
            print(semaforo) # Opción incorrecta
    else:
            print("Opción incorrecta")


actividad2()


def actividad3():
    print("actividad3")
    #Escribe el código para dos números a y b, el usuario va a seleccionar una opcion: 
        #1 para sumar, 2 para multiplicar, 3 para restar (a-b) y 4 para dividir (a/b) y 
        #retornar el resultado de la operación indicada.

    print("[1] Suma")
    print("[2] Resta")
    print("[3] Multiplicación")
    print("[4] División")

    operacion = int(input("Dígite su opción [1-4]: "))

    num1= int(input("numero 1: "))
    num2= int(input("numero 2: "))

    if (operacion == 1):
        total = num1 + num2
        return (f"{num1} + {num2} = {total}")
    elif operacion == 2:
        total = num1 - num2
        return (f"{num1} - {num2} = {total}")
    elif operacion == 3:
        total = num1 * num2
        return (f"{num1} * {num2} = {total}")
    elif operacion == 4:
        total = num1 / num2
        return (f"{num1} / {num2} = {total}")
    else:
        return ("La opción ingresada es incorrecta.")

# Ejecutamos e imprimimos la operacion de la activadad 3
print(actividad3())






