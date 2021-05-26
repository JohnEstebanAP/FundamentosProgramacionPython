#1. leer un nùmero de 4 dígitos mostrar el dígito mayor e informar si es par o impar
#num % 10: me devuelve el ultimo dígito    4322 % 10 => 2
#int(hum/10): elimina el ultimo dígito.
#hum // 10: elimina el ultimo dígito.
num = int(input("Digite el numero de 4 dígitos: "))

digNum1 = num % 10
digNum2 = (num // 10) % 10
digNum3 = (num //100) % 10
digNum4 = (num // 1000) % 10

if (digNum1 > digNum2 and digNum1 > digNum3 and digNum1 > digNum4 ):
    NumMayor = digNum1
elif digNum2 > digNum1 and digNum2 > digNum3 and digNum2 > digNum4:
    NumMayor = digNum2
elif (digNum3 > digNum1 and digNum3 > digNum2 and digNum3 > digNum4):
    NumMayor = digNum3
else:
    NumMayor = digNum4

if (NumMayor % 2) == 0:
    siPar= "PAR"
else:
    siPar= "IMPAR"

print(f"El dígito mayor es {NumMayor} y es {siPar}.")


'''
# Código del Profesor
#4321
mayor = num % 10 #1
num = int(num/10) #432
test = num % 10 #2

if (mayor <  test):
    mayor = test #2
    num = int(num/10) #43
    test = num % 10 # 3

if (mayor < test):
    mayor = test #3
    num = int(num/10) #4
    test = num % 10 #4

if (mayor <  test):
    mayor= test # 4

parImpar = "IMPAR"
if mayor % 2 == 0:
    parImpar = "PAR"

print(f"El dígito mayor es {NumMayor} y es {siPar}.")
'''