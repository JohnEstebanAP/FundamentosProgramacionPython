for i in "Laura":
    print(i)

for  i in ["Invierno","Primavera","Verano","Otoño"]:
    print(i)

i = 0
print("-con el While:")
while i < 3:
    print(i)
    i += 1

print("Con rango 3") 
for i in range(3):
    print(i)

print("Con rango 6") 
for i in range(0,6):
    print(i)

print("Con rango de 5 a 10")
for i in range(5,11):
    print(i) 

print("Con de 2 a 20 y incremento de 2")
# inicia en 2 hasta el 20 incluyendo, con incremento de ds en dos.
for i in range(2,21,2):
    print(i)


#Con decimales no es posible utilizar el rango
#tienen que ser números enteros.
'''
for i in range(5.5):
    print(i)
'''

print("prueba de rango")
num= range(2,10,2)
print(num[0])

print(num[2])

