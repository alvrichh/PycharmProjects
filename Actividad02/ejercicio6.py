'''
Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por
pantalla la misma frase pero con la vocal introducida en mayúscula.
'''
frase = input("Por favor, introduce una frase: ")
vocal = input("Por favor, introduce una vocal: ")

if len(vocal) == 1 and vocal in 'aeiouAEIOU':
    frase_modificada = frase.replace(vocal, vocal.upper())
    print("Frase con la vocal en mayúscula:", frase_modificada)
else:
    print("La entrada no es válida. Por favor, introduce una única vocal.")
