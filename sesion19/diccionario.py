profesor = { 
    "ide" : 1, 
    "codIde" : 8526, 
    "nom" : ["Hernaldo","Rafael"], 
    "ape" : ["Peñaranda", "Bello"],
    "tel" : {"trabajo":[318],"personal":[311421,874]}
}

print(f"Id:", profesor["ide"])
print(f"C.C:", profesor["codIde"])
print("Primer nombre:", profesor["nom"][0])
print("Segundo nombre:", profesor["nom"][1])
print("Primer Apellido:", profesor["ape"][0])
print("Segundo Apellido:", profesor["ape"][1])
print("Teléfono del trabajo:", profesor["tel"]["trabajo"][0])
print("Teléfono (1) personal:", profesor["tel"]["personal"][0])
print("Teléfono (2) personal:", profesor["tel"]["personal"][1])