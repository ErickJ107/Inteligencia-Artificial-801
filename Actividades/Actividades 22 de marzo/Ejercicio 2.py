usuario = input("Usuario: ")
password = input("Contraseña: ")

if usuario == "admin" and password == "secreto123":
    print ("Acceso concedido.")
elif usuario != "admin":
    print ("Usuario incorrecto.")
else:
    print ("Contraseña incorrecta.")