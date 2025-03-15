import random

opciones = ["piedra", "papel", "tijera"]

user = str(input("Elige piedra, papel o tijera: "))

cpu = random.choice(opciones)
print (f"La computadora eligió: {cpu}")

if user == cpu:
    print ("Empate")
elif (user == "piedra" and cpu == "tijera") or \
    (user == "papel" and cpu == "piedra") or \
    (user == "tijera" and cpu == "papel"):
    print ( "¡Ganaste!")
else:
    print ("¡Perdiste")