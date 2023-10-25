"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe
mostrar por pantalla la paga que le corresponde.
"""
h = float(input("Número de horas trabajadas: "))

c = float(input("Coste por hora: "))

paga = str(h * c)

print("Paga correspondiente: " + paga)

