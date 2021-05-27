#Diseñe un algoritmo que calcule el promedio de notas
# del primer parcial de un grupo de n estudiantes

n = int(input("Digité la cantidad de estudiantes: "))

acuNota = 0
contador = 0

while contador < n:
    nota = float(input("Digité su nota: "))
    acuNota = acuNota + nota
    contador +=1

promedio = acuNota / n

print("El promedio de la nota de los {0} estudiantes es igual a {1:0.2f}.".format(n,promedio))
