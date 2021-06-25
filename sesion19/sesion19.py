"""
Manejo de archivos

Continuemos ahora con otras opciones como escribir y actualizar un archivo desde Python.

Recordemos las opciones disponibles para el manejo de archivos.
Modo 	Descripción
'r' 	Abrir el archivo en modo lectura, este es el valor por defecto
'w' 	Abrir el archivo para escritura, eliminará cualquier archivo existente con el mismo nombre
'x' 	Crear el archivo, si existe uno con el mismo nombre sacará un error
'a' 	Abrir el archivo para escribir. Todo lo escrito se adicionará al final del archivo
'b' 	Abrir en modo binario
't' 	Abrir en modo texto, este es el valor por defecto
'+' 	Abrir para lectura y escritura

Empecemos creando un archivo de texto llamado minuevoarchivo.txt. 
"""
def ejemplo1():
    nuevoArchivo = open('minuevoarchivo.txt', mode='w', encoding='utf-8-sig' )
    nuevoArchivo.write("Escribiendo desde Python")

ejemplo1()

#Ahora vamos a crear un diccionario y a imprimir todos los valores y el valor almacenado con la clave 2
def ejemplo2():
    diccionario = { 1 : 'lunes', 2:'martes', 3:'miercoles', 4:'jueves', 5:'viernes', 6:'sabado', 7:'domingo'}

    print(diccionario)
    print(diccionario[2])

ejemplo2()

# Actividad 1
#
# Vamos a elaborar un algoritmo que permita ingresar un número entero (1 a 10), y muestre su equivalente en romano usando un diccionario como lo definimos anteriormente. 
def numerosRomanos():
    
    while True:       
        try:        
            dato= input("Por favor ingrese un numero \ndel 1 al 10 para determinar su numero romano\n: ")
            numRomanos = {
                "1":"I",
                "2":"II",
                "3":"III",
                "4":"IV",
                "5":"V",
                "6":"VI",
                "7":"VII",
                "8":"VII",
                "9":"IX",
                "10":"X"
            }
            print(f"el numero {dato} en numero romanos es ",numRomanos[dato])
            break
        except KeyError:
            print("El numero ingresado no es un numero en el rango del 1-10")        




#Actividad 2 
#Recordemos una de las actividades que hicimos en sesiones anteriores.
#
#Diseña un programa con las siguiente características:
#
#    Que tenga una función caja que 
#       a. Cree un archivo recibo.txt
#       b. Solicite al usuario nombre y precio de cada producto.
#       d. Una función adicional llamada guardaProducto(nombre, precio, archivo) que reciba el nombre y el precio de cada producto y los escriba en el archivo recibo.txt.
#       e. Que después de llamar a guardaProducto le pregunte al usuario si tiene o no más artículos a ingresar. Si no tiene, el programa debe detenerse.
#    Al final de tus funciones, puedes simplemente llamar a la función caja para probar

from io import open_code
def guardarProducto(nombre, precio):
    miArchivo = open("recibo.txt","a")
    miArchivo.write(f"{nombre},{precio}\n")
    miArchivo.close()  

def caja():
    continuar = True
    while continuar:
        nomProducto = input("Escriba el nombre del producto: ")
        valProducto = int(input(f"Digite el valor del {nomProducto}: "))

        guardarProducto(nomProducto, valProducto)

        continuar = input("¿Dese agregar más productos [S/N]?: ").upper()#lo pasa todo al mayúsculas
        if continuar != "S":
            continuar = False
        else:
            continuar = True

def activadad2():
    print("Actividad 2:\n")
    caja()



if __name__ == "__main__":
    #numerosRomanos()
    activadad2()