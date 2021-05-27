#Condicionales múltiples caso elif

#Crear una calculadora con las operaciones básicas

print("[1] Suma")
print("[2] Resta")
print("[3] Multiplicación")
print("[4] División")

operacion = int(input("Dígite su opción [1-4]: "))

num1= int(input("numero 1: "))
num2= int(input("numero 2: "))

if (operacion == 1):
    total = num1 + num2
    print (f"{num1} + {num2} = {total}")
elif operacion == 2:
    total = num1 - num2
    print (f"{num1} - {num2} = {total}")
elif operacion == 3:
    total = num1 * num2
    print (f"{num1} * {num2} = {total}")
elif operacion == 4:
    total = num1 / num2
    print (f"{num1} / {num2} = {total}")
else:
    print("La opción ingresada es incorrecta.")
