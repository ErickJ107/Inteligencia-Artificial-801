try:
    cuenta = float(input("Ingrese el total de su cuenta: "))

    print("Seleccione el porcentaje de propina:")
    print("1. Nada")
    print("2. 10%")
    print("3. 15%")
    print("4. 20%")

    opcion = int(input("Ingrese el número de su elección: "))

    if opcion == 1:
        propina = 0.0
    elif opcion == 2:
        propina = 0.10
    elif opcion == 3:
        propina = 0.15
    elif opcion == 4:
        propina = 0.20
    else:
        print("Opción inválida. No se agregará propina.")
        propina = 0.0

    total_pagar = cuenta + (cuenta * propina)
    print(f"El total a pagar, incluyendo propina, es: ${total_pagar:.2f}")

except ValueError:
    print("Error: Por favor, ingrese un número válido.")