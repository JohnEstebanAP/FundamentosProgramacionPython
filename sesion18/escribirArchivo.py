from io import open

#Persistencia 
# tomar el control de un archivo que se encuentra 
# dentro del disco duro. 

# a ... append
# w ... escriba información en el archivo pero borra todo lo que tenia anteriormente
# r ... lectura
# r+ ... lectura y escritura
# rb ... lectura binarios
# wb ... Escritura binaria

file = open("archivo.txt","w")

file.write("Hola mundo")
file.write("\nEjemplar")
file.write("\nSegundo ejemplar")
file.write("\nTercer ejemplar")

# siempre qeu abrimos un archivo lo debemos serra
file.close()