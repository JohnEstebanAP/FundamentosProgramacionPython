print("Funcion 2.")
#   2. Leer dos números de 3 dígitos cada uno, formar un tercer número 
#      con el mayor del primero y el menor del segundo.

num1 = int(input("Digite el primer numero de 3 dígitos: "))
num2 = int(input("Digite el segundo numero de 3 dígitos: "))






#Calculamos el Numero Mayor del primero
digNum1 = num1 % 10
digNum2 = (num1 // 10) % 10
digNum3 = (digNum1 //100) % 10

numMayor = digNum1

if numMayor < digNum2:
    numMayor = digNum2
if numMayor < digNum3:
    numMayor = digNum3

print("\n")
print(f"El dígito mayor es {numMayor}")

#Calculamos el numero  menor del segundo.

digNum1 = num2 % 10
digNum2 = (num2 // 10) % 10
digNum3 = (num2 //100) % 10

numMenor = digNum1

if numMenor > digNum2:
    numMenor = digNum2
if numMenor > digNum3:
    numMenor = digNum3


print(f"El dígito Menor es {numMenor}")
print("\n")

# Formar un tercer número 
# con el mayor del primero y el menor del segundo.

newNum = str(numMayor) + str(numMenor)
print(f"El nuevo numero es {numMayor} + {numMenor} es: {newNum}")







'''
#Calculamos el Numero Mayor del primero

digNum1 = num1 % 10
digNum2 = (num1 // 10) % 10
digNum3 = (num1 //100) % 10

if (digNum1 > digNum2 and digNum1 > digNum3  ):
    NumMayor = digNum1
elif digNum2 > digNum1 and digNum2 > digNum3:
    NumMayor = digNum2
else:
    NumMayor = digNum3

print("\n")
print(f"El dígito mayor es {NumMayor}")





#Calculamos el numero  menor del segundo.

digNum1 = num2 % 10
digNum2 = (num2 // 10) % 10
digNum3 = (num2 //100) % 10

if (digNum1 < digNum2 and digNum1 < digNum3  ):
    numMenor = digNum1
elif digNum2 < digNum1 and digNum2 < digNum3:
    numMenor = digNum2
else:
    numMenor = digNum3

print(f"El dígito Menor es {numMenor}")
print("\n")

# Formar un tercer número 
# con el mayor del primero y el menor del segundo.

newNum = str(NumMayor) + str(numMenor)
print(f"El nuevo numero es {NumMayor} + {numMenor} es: {newNum}")
'''