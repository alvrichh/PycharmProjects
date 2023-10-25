"""
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe
mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""
p = 3.49

d = 0.60

n = int(input("Número de barras de pan vendidas que no son del día: "))

t = round((p * d * n), 2)

print("El precio de las barras de pan está a: " + str(p)
      + "\nCon el descuento están a: " + str(p * d)
      + "\nUsted a comprado: " + str(n) + " barras de pan que no son del día."
      + "\nEl precio total es: " + str(t))
