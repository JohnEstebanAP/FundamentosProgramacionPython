try:

    while True:

        # se solicitan los datos para la división:
        x = int(input("Digite el numerador: ")) # valor del numerador
        y = int(input("Digite el denominador: ")) # valor del denomidador
        res = x / y
        print(f"{x}/{y} = {res}")
        break

except ValueError:
    print("¡Debe digitar un número!")
except ZeroDivisionError:
    print("¡El denominador debe ser diferente de cero (0)!")
except:
    print("¡Error desconocido, vuelva a intentar! ")
