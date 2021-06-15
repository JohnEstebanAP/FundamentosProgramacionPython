from io import open

file = open("archivo.txt","r+")


frase = "Esto es una modificación\n"

file.write(frase)

file.seek(0)
contenido = file.read()

print(contenido)
file.close()