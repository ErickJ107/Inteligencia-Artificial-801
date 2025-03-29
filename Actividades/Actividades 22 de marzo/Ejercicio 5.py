respuesta = ""
intentos = 0
maximo_intentos = 3

while respuesta.lower() != "python" and intentos < maximo_intentos:
    respuesta = input("¿Cual es el mejor lenguaje de programación?: ")
    intentos += 1

    if respuesta == "python":
        print ("¡Correcto!")
    break

if respuesta != "python":
    print ("Número de intentos alcanzado")