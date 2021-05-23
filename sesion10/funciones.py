# Prueba y explicación del uso de funciones y como retornar un valor
def sumar(n1,n2):
 suma = n1 + n2
 return suma

print(sumar(5,5))


n1 = 4
n2 = 5
n3 = 4

def numerador():
    suma = n1 + n2 + n3
    return suma

def denominador():
    return 3

def ciudades():
    lista = []
    for i in range(3):
        ciudad = input(f"Digite la ciudad {i+1}: ")
        lista.append(ciudad)
    
    return lista


print(ciudades()[0])





#Las combinaciones o coeficientes binomiales son una serie de números que indican 
# la cantidad de formas en que se pueden extraer subconjuntos a partir de un conjunto dado.
#Para calcular combinaciones se debe utilizar la siguiente fórmula:

def factorial(z):
    factorial = 1
    for i in range(1,z+1):
        factorial = factorial * i
        
    return factorial    
  
    
if __name__ == "__main__":
    n = int(input("Digite la cantidad de elementos: "))
    m = int(input("Digite la cantidad de los subconjuntos: "))

    combinacion = factorial(n) / (factorial(m) * factorial(n-m))

    print(f"{n}C{m} = {int(combinacion)}")
