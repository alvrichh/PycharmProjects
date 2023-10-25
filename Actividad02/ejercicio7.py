'''
Ejercicio 7
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo
electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio iesalixar.org
'''
email = input("Por favor, introduce tu correo electrónico: ")

# Dividir el correo electrónico en nombre de usuario y dominio
nombre_usuario, dominio = email.split('@')

# Crear el nuevo correo electrónico con el dominio "iesalixar.org"
nuevo_email = nombre_usuario + '@iesalixar.org'

print("Nuevo correo electrónico:", nuevo_email)
