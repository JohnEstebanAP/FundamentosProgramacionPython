while True:
    try:
        dato = input("Digite el sexo [1/2/M/F/Masculino/Femenino/Mujer/Hombre] \n:")

        genero = { 
            "1":"Masculino",
            "M":"Masculino",
            "Masculino":"Masculino",
            "Hombre":"Masculino",
            "2":"Femenino",
            "F":"Femenino",
            "Femenino":"Femenino",
            "Mujer":"Femenino"
        }
        print(genero[dato]) #Masculino/Femenino

        break
    except KeyError:
        print("¡Error,el dato no es válido! Por favor vuelva a intentar...")