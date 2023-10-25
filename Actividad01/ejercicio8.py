"""
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c>
y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de
la división entera respectivamente.
"""
n = int(input("Introduce un número: "))

m = int(input("Introduce otro número: "))

c = n//m

r = n % m

print(str(n) + " entre " + str(m) + " da un cociente " + str(c) + " y un resto " + str(r))
