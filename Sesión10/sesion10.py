"""
Funciones

La verdad es que hemos venido trabajando con funciones desde que empezamos con archivos .py 
En Python, definimos una función con la siguiente estructura

def función(parametros)

Recuerda que los parametros son opcionales!
"""

def suma(a,b):
    
    print(a+b)

suma(3,4)


#Actividad 1
#Usted es cajero en un supermercado de su ciudad. Su trabajo es imprimir cada uno de los productos de su cliente, su precio y calcular el total a pagar.
#
#Diseña un programa con las siguiente características:
#
#    1. Que tenga una función caja que solicite al usuario nombre y precio de cada producto.
#    2. Una variable total que vaya sumando el precio de los artículos
#    3. Una función adicional llamada imprimaProducto(nombre, precio) que reciba el nombre y
#        el precio de cada producto y los imprima.
#    4. Que después de llamar a imprimaProducto le pregunte al usuario si tiene o no más artículos a ingresar. Si no tiene, el programa debe detenerse.
#    5. Si no hay más artículos, que imprima el total de la compra

#    Al final de tus funciones, puedes simplemente llamar a la función caja para probar

#caja()


def imprimirProducto(producto,precio):
    print(f"El producto {producto} con precio de {precio}.")
    return
 
def caja():
    i = True
    totalFactura = 0
    while i == True:
        producto = input("Escribir el nombre del producto: ")
        precio = int(input(f"Digite el precio de {producto}: "))
        imprimirProducto("producto",precio)
        totalFactura = totalFactura+ precio
        continuar = input("¿Desea ingresar mas producto? [si / no]: ")
        if continuar == "NO" or continuar == "No" or continuar == "no" or continuar == "n":
            print(f"El total de la compra es: {totalFactura}")
            i = False




#Actividad 2
#
#Escribamos una función numAleatorio() que retorne un número aleatorio entre 100 y 130, 
#excepto los números 110, 115 y 120 .
#
#Adicionalmente, una función números que imprima diez números aleatorios 
#(retornados por la función numAleatorio()) alternando par, impar, comenzando por par.
import random
def numerosAleatorio():
    continuar = True
    while continuar:
        num = random.randint(100,130)
        if num != 110 and num != 115 and num != 120:
            return num
            break

def numeros():
    par = True
    for i in range(10): 
        if par == True:
            par = False
            num = numerosAleatorio()
            while num % 2 != 0:
               num = numerosAleatorio()
            print(num)
        else:
            par = True
            num = numerosAleatorio()
            while num % 2 == 0:
                num = numerosAleatorio()
            print(num)

if __name__=="__main__":
    #caja()
    numeros()

