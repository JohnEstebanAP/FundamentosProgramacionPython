from io import open

file = open("archivo.txt","r")


lista = file.readlines()
'''
['Hola mundo\n', 
 'Ejemplar\n', 
 'Segundo ejemplar\n', 
 'Tercer ejemplar']
'''

print(lista)
file.close()