"""
Ejercicio 11
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una
cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de
unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""
nombre_producto = input("Ingresa el nombre del producto: ")
precio_unitario = float(input("Ingresa el precio unitario del producto: "))
numero_unidades = int(input("Ingresa el número de unidades: "))

# Calcular el coste total
coste_total = precio_unitario * numero_unidades

# Mostrar la información formateada
print("Producto:", nombre_producto)
print("Precio Unitario: {:0.2f}".format(precio_unitario))
print("Número de Unidades: {:03d}".format(numero_unidades))
print("Coste Total: {:0.2f}".format(coste_total))
