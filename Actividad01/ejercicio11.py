"""
Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a
intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un
programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
Redondear cada cantidad a dos decimales.
"""
i = 0.04

c = float(input("Introduce la cantidad a invertir: "))

a1 = round(c * (1 + i), 2)

a2 = round(a1 * (1 + i), 2)

a3 = round(a2 * (1 + i), 2)

print("\nAhorros generados:"
      + "\n\tPrimer año: " + str(a1)
      + "\n\tSegundo Año: " + str(a2)
      + "\n\tTercer Año: " + str(a3))
