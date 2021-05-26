#Escriba un programa qeu pida un año y que escriba si es bisiesto o no 
#Cualquier año divisible por 4 es un año bisiesto
#Por ejemplo: 1988, 1992 y 1996 son años bisiestos

#estos, años no son años bisiestos:
# 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600

#Los años siguientes son años bisiestos 1600, 2000, 2400
#

year = int(input("Digite el año: "))

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("El año {year} es bisiesto.")
elif year % 4 == 0 and year % 100 != 0:
    print("el año {year} es bisiesto.")
else:
    print("el año {year} no es bisiesto.") 
