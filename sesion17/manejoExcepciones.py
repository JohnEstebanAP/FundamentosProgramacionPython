
while True:
    try:
        x = int(input("Digite el numerador: "))
        y = int(input("Digite el denominador: "))

        res= x / y
        print(f"{x} / {y} = {res}")
        break
    except ValueError: # validar si escribió una letra.
        print("Error debe escribir un número, por favor vuelva a intentar.")
    except ZeroDivisionError: # validar si escribió un valor diferente de zero en el denominador.
        print("¡Error, el denominador tiene que ser diferente de 0 !")
    except: #Validar cualquier otro error no conocido.
        print("¡Error no registrado!")