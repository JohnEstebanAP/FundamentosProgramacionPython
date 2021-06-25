import pickle

# Escribir en el archivo binario
miArchivo= open("archivoBinario.txt", mode="wb")

pickle.dump("primera Linea\n",miArchivo)
pickle.dump("seunda linea\n",miArchivo)

miArchivo.close()

#Leer en el archivo binario:

miArchivo= open("archivoBinario.txt", mode="rb")

contenidoBinario = pickle.load(miArchivo)
print(contenidoBinario)

contenidoBinario = pickle.load(miArchivo)
print(contenidoBinario)


miArchivo.close()


