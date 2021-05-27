#Escriba un programa que pida tres números y que escriba si son iguales,
# hay dos iguales o son distintos.

print ("Por favor Escriba 3 números")

print ("Numero 1: ")
num1= int(input())

print ("Numero 2: ")
num2= int(input())

print ("Numero 3: ")
num3= int(input())

# Lógica estudiando el caso
#Condicional para verificar que números son y guales
if(num1 == num2 and num1 == num3 ):
    print("todos los números son iguales")  
elif(num1 != num2 and num2 != num3 and num1 != num3):
    print("todos los números son Diferentes")
else:
    print("dos números son iguales")



    '''
cont=1  # Contador para saber cuantos números son iguales
#Condicional para verificar que números son y guales
if(num1 == num2):
    cont = cont+1

    if(num1 == num3 ):
        cont = cont+1    
elif (num2 == num3):
    cont = cont+1
elif (num1 == num3):
    cont = cont+1

if(cont == 2):
    print("dos números son iguales")
elif(cont == 3):
    print("todos los números son iguales")
else:
    print("todos los números son Diferentes")
'''