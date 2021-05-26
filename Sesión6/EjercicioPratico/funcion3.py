print("FUNCIÓN 3.")
#3. Leer un número de 3 dígitos y formar el mayor número posible 
#      con sus cifras.
#Escribe el código de la tercera opción aquí
#num % 10: extraer el último dígito.
#int(num/10): elimina el último dígito.
#num//10: elimina el último dígito.
#int(num/100): elimina los dos últimos dígitos.
#int(num/1000): elimina los tres últimos dígitos.


num = int(input("Digite un número de 3 dígitos: ")) # 852

d3 = num%10 #  2
d2 = int(num/10)%10 #  5
d1 = int(num/100)%10 #  8

mayor = d3 # 2
nNum = int(str(d1) + str(d2))  # 85

if mayor < d2:
    mayor = d2 # 5
    nNum = int(str(d1) + str(d3))  # 82
if mayor < d1:
    mayor = d1 # 8
    nNum = int(str(d2) + str(d3))  # 52


d2 = nNum%10 #  2
d1 = int(nNum/10)%10 #  5

if d2 < d1:
    nNum = int(str(mayor) + str(d1) + str(d2))
else:
    nNum = int(str(mayor) + str(d2) + str(d1))

print(f"El nuevo número formado por {num} es {nNum}.")




