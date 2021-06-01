"""

Para

El ciclo Para o For en Python nos ayuda a ejecutar dentro dentro de un rango determinado de iteraciones. 


En la semana uno exploramos el tipo de dato string (una cadena de caracteres). 
Los caracteres dentro de este tipo de dato en Python puede ser recorridos con la posición en la que se encuentran dentro de la cadena. Veamos un ejemplo:
"""

def ejemplo1():
    palabra = "Prueba"
    longitud = len(palabra)

    print("Primer ciclo")
    for i in range(longitud):
        print(palabra[i])

    print("Segundo ciclo")
    for x in "Prueba":
        print(x)

#ejemplo1() 


def actividad1():
    print("actividad1")
    # Vamos a realizar un algoritmo que nos calcule la serie de Fibonacci.
    # La serie o secuencia de Fibonacci comienza con los números 0 y 1 y 1, y a partir de allí es posible calcular el siguiente valor como la suma de los dos valores anteriores. 
    # Por ejemplo, 1+1=2, 1+2=3, 2+3=5, etc. Así, los primeros números de la secuencia son: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    # Creemos un programa que a partir de un número N ingresado, imprima los primeros N números de la serie de Fibonacci.
 
    n = int(input("Ingrese el número n al que desea llegar en la serie fibonacci: "))
    num1 = 0
    num2 = 0
    tem = 1
    for i in range(n):
        print(num1)
        num2 = tem
        tem = num1
        num1 = num1 + num2

#actividad1()

def actividad2():
    print("actividad2")
    #Escribe el código usando break que reciba una palabra e imprima el número de letras que tiene y las letras hasta que, o bien termine la palabra o encuentre la letra a. .
    palabra = (input("Ingrese una palabra: "))
    for i in palabra:
        if i == "a":
            break
        print(i)

#actividad2()

def actividad3():
    print("actividad3")
    #Escribe un algoritmo que lea 10 números e imprima cuantos son positivos, cuantos negativos y cuantos neutros(0).
   
    contadorPosi = 0
    contadorNega = 0
    contadorNeutros = 0
    print("Ingrese 10 números enteros ")

    for i in range(10):
        num = int(input(f"Ingrese el número {i+1}: "))

        if num == 0:
            contadorNeutros += 1
        elif num > 0:
            contadorPosi += 1
        else:
            contadorNega += 1
        
    print("neutros: ",contadorNeutros)
    print("positivos: ", contadorPosi)
    print("Negativos: ", contadorNega)     

#actividad3()

def actividad4():
    print("actividad4")
    #Usando tanto while como for, escribe el código que pida números al usuario hasta que este ingrese -1 y que retorne el factorial de cada número ingresado usando un ciclo Para (For).
    num1= 0
    numFactorial = 1
    while num1 != -1:
        num = (input("Ingrese un numero para calcular su factorial: "))
    
        if num == "":
            print("No ingreso ningún numero")
            continue

        num1 = int(num)
        if num1 == -1:
            print("¡FIN!")

        else:   
            numFactorial = 1
            for i in range(1,num1+1):
                numFactorial = numFactorial * (i)
            print(f"factorial de {num1}: {numFactorial}")
actividad4()