saldo = 10000
opcion = ""

while opcion != "Salir":
    print ("\n1. Consultar saldo\n2. Retirar\n3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print ("Saldo actual:", saldo)
    elif opcion == "2":
        cantidad = int(input("¿Cuanto desea retirar?: "))
        if cantidad <= saldo:
            saldo -= cantidad
            print ( "Retiro exitoso. Saldo:", saldo)
        else:
            print ("Sin dinero, das lastima.")
    elif opcion == "3":
        opcion = "Salir"
    else:
        print ("Opcion no valida")