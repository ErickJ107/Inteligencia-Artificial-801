edad = int(input("Introduce tu edad: "))

if edad < 13:
    print ("Eres un niño.")
elif edad < 18:
    print ("Eres un adolecente.")
elif edad >=18 and edad <29:
    print ("Adulto joven")
elif edad < 60:
    print ("Eres adulto")
else:
    print ("Eres un adulto mayor")