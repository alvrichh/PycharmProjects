'''
Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se
introduzcan con un solo carácter.
'''
preg = input("Introduzca su fecha de nacimiento (dd/mm/aaaa): ")
res = preg.split('/')

print("Dia: ", res[0], "\nMes: ", res[1], "\nAño: ", res[2])
