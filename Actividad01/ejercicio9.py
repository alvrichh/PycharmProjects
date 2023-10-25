"""
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y
muestre por pantalla el capital obtenido en la inversión.
Cantidad a invertir * (Interés Anual / 100 + 1) ^ Número de Años
"""
c = float(input("Introduce la cantidad a invertir: "))

i = float(input("Introduce el interés anual: "))

a = float(input("Introduce el número de años: "))

g = c * (i * a)

print("Capital obtenido en la inversión: " + str(g))
