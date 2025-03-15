edad = int(input("Introduce tu edad: "))

if edad < 18:
    print ("¡Lo siento, no puedes entrar!")
elif edad >=18 and edad <=21:
    print ("Puedes entrar, pero sin bebidas alcohólicas")
else:
    print ("Bienvenido!")