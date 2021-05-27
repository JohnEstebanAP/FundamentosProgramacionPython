"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

La opción break, puede parar el ciclo aunque la condición sea real. Por ejemplo:
"""

def ejemplo1():
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1 
#ejemplo1()

def actividad1():
    print("actividad1")
    # Continuemos integrando los conceptos que hemos visto hasta el momento. 
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número pero que termine el proceso si llega al 10.

    num = int(input("ingrese un número por favor: "))
    i=0
    while i < (num-1):
            i +=2
            print(i)
            if i == 10:
                break
#actividad1()

"""
La opción continue, puede continuar el ciclo y saltarse cuando sea verdadera. Por ejemplo:
"""
def ejemplo2():
    i = 1
    while i < 6:
        if i == 3:
            i += 1 
            continue
        print(i)
        i += 1 

#ejemplo2()

def actividad2():
    print("actividad2")
    #Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario pero saltarse si el digito es 4.

    num = int(input("Digité su número: "))
    contador = 0

    while num > 0:
        if num % 10 == 4:
            num = int(num / 10)
            continue 
        num = int(num / 10)
        contador = contador + 1
    print(f"La cantidad de dígitos es de: {contador}.")
    
actividad2()