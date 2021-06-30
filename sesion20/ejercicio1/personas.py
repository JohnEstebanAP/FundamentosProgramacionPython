from io import open
#id,nombre, apellido y nacimiento.

#Ejercicio 1
#En este ejercicio deberas crear un script llamado personas.py
#que lea los datos de un archivo de texto,
#que transforme cada fila en un diccionario y lo añada a una lista llamada personas.

def leerArchivo(archivo):
    miArchivo = open(archivo, mode="r")
    lista = miArchivo.readlines()
    miArchivo.close()
    return lista

def transformar(archivo):
    lista = leerArchivo(archivo)

    persona = []

    for fila in lista:
        fila = fila.strip("\n").split(";")
        diccionario = {}
        diccionario["id"]=fila[0]
        diccionario["nombre"]= fila[1]
        diccionario["apellido"]= fila[2]
        diccionario["nacimiento"]= fila[3]
        persona.append(diccionario)
    
    return persona

def imprimirListaDiccionario(archivo):
    personas = transformar(archivo)
    for fila in personas:
        print("Id:",fila["id"],"  Nombre:",fila["nombre"],fila["apellido"], "  Fecha:",fila["nacimiento"])


if __name__=="__main__":
    archivo = "personas.txt"
    imprimirListaDiccionario(archivo)
