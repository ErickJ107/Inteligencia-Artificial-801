def edad_humana(mascota, edad):
    if mascota.lower() == "perro":
        return edad * 7
    elif mascota.lower() == "gato":
        return edad * 5
    else:
        return "Tipo de mascota no válido. Usa 'perro' o 'gato'."

mascota = input("Introduce el tipo de mascota (perro/gato): ")
edad = int(input("Introduce la edad de la mascota en años: "))

edad_convertida = edad_humana(mascota, edad)
print(f"La edad de tu {mascota} en años humanos es: {edad_convertida}")