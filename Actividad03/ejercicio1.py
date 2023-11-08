"""
Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""
preg = input("¿Cuantos años tienes?  ")

if int(preg) < 0:
    print("La edad no puede ser negativa")
elif int(preg) >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")