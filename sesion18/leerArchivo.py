from io import open

file = open("archivo.txt","r")

file.seek(10)   
# Me permite empezar desde 
# la posición del puntero.

contenidio = file.read()
print(contenidio
)

file.seek(0)
contenidio = file.read()
print(contenidio)

file.seek(0)
contenidio = file.read(20)
# solo lee asta la posicion 20
print(contenidio, end="")

file.close()