from io import open

file = open("archivo.txt","r")

linea = file.readline()

print(linea, end = "")

linea = file.readline()
print(linea)

file.close