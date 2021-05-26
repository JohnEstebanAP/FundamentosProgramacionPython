#Actividad 1
#Los tipos de datos son muy importantes 
# en programación. Aunque Python no 
# exige declarar un tipo de variable y 
# permite cambiarlo (lo cual no ocurre 
# en otros lenguajes de programación), 
# cada variable si asume un tipo según 
# el dato que tenga almacenado. 
# Por ejemplo:

a = 5     # Esto es un Entero (No tiene decimales)
b = 5.3   # Esto es un flotante (Un número que puede tener comas decimals)
c = '5'   # Esto es un texto, y por ende, no podemos hacer operaciones matemáticas con c

# Usando la función type(), obten e imprime el tipo de dato de las variables a, b y c:
print(type(a))
print(type(b))
print(type(c))



#Actividad 2
#Ahora, practiquemos nuevamente la estructura algorítmica y 
# recordeºmos el uso de tipos de datos.

#Juan y Pedro acostumbran jugar un juego de adivinar un número. 
# En el juego es permitido dar tres pistas p1 p2 p3. 
# Después de muchos intentos Pedro descubre la fórmula
#  con la que Juan crea el número con las pistas dadas,
#  y es la siguiente:

# p1 + p3 ∗ p2 − (p1 + p2 ∗ 5 + 1) / (p2 + p1/2) + p3

#Si la pista que da Juan es 2, 1 y 4, 
# ¿cuál es el número que debería decir Pedro para ganar? 
# Escribamos el código para recibir los valores 
# y devolver el valor que Pedro debería decir.

p1=2
p2=1
p3=4

total= p1 + p3 * p2 - (p1 + p2 * 5 + 1) / (p2 + p1/2) + p3
print("El número es:", total)