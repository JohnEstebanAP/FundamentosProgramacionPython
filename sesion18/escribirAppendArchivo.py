from io import open

file = open("archivo.txt","a")

frase = "Esto va al final -"
numero = 11000
file.write("\n" + str(numero) + "\n" + frase)


file.close()