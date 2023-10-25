'''
Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla
el número de euros y el número de céntimos del precio introducido.
'''
precio = input("Por favor, introduce el precio del producto en euros (con dos decimales): ")

# Extraer la parte entera y la parte decimal del precio
euro = precio.split('.')

print("El precio ingresado es: ", euro[0], " y ", euro[1], " céntimos.")
