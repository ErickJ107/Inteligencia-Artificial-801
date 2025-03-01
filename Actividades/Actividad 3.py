def calculadora():
    while True:
        try:
            num = int(input("Ingrese un número: "))
            if num <= 0:
                print("Error: El número debe ser mayor que cero. Inténtelo nuevamente.")
                continue
        except ValueError:
            print("Error: Debe ingresar un número válido.")
            continue
        
        print("Seleccione una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        
        opcion = input("Ingrese el número de la operación deseada: ")
        
        if opcion not in ["1", "2", "3", "4"]:
            print("Error: Opción no válida. Inténtelo nuevamente.")
            continue
        
        try:
            otro_num = int(input("Ingrese otro número: "))
            if otro_num <= 0:
                print("Error: El número debe ser mayor que cero.")
                continue
        except ValueError:
            print("Error: Debe ingresar un número válido.")
            continue
        
        if opcion == "1":
            resultado = num + otro_num
            operacion = "suma"
        elif opcion == "2":
            resultado = num - otro_num
            operacion = "resta"
        elif opcion == "3":
            resultado = num * otro_num
            operacion = "multiplicación"
        elif opcion == "4":
            if otro_num == 0:
                print("Error: No se puede dividir entre cero.")
                continue
            resultado = num / otro_num
            operacion = "división"
        
        print(f"El resultado de la {operacion} entre {num} y {otro_num} es: {resultado}")
        
        otra_vez = input("¿Desea realizar otra operación? (s/n): ")
        if otra_vez.lower() != "s":
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
calculadora()