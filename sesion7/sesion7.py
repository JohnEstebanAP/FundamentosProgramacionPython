# Ciclos mistras que (while)

def ejemplo1():
    i = 1
    while i < 6:
        print(i)
        i += 1
ejemplo1()

def actividad1():
    print("actividad1")
    # Continuemos integrando los conceptos que hemos visto hasta el momento. 
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número. 

    num = int(input("ingrese un número por favor: "))
    i=0
    while i < (num-1):
            i +=2
            print(i)

#actividad1()


def actividad2():
    print("actividad2")
    #Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario.

    num = int(input("Digite su número: "))
    contador = 0

    while num > 0:
        num= int(num / 10)
        contador += 1

    print(f"La cantidad de digitos es de: {contador}.")
actividad2()    
    

def actividad3():
    print("actividad3")
    #Escribe el código que solicite números al usuario hasta que éste ingrese -1.
    #Cuando se ingrese -1, el programa debe imprimir el promedio de todos los números ingresados hasta ese momento (sin contar con el -1).
    i=1
    n= 100
    contador = 0
    promedio = 0
    print("Ingresa -1 para calcular el promedio")
    while i < n:
        num1 = int(input("Ingresa un numero: "))
        if num1 == -1:
            i=100
        else:
            contador += 1
            promedio =  promedio + num1
    promedio= promedio / contador

    print(f"El promedio es de: {promedio}")

actividad3()