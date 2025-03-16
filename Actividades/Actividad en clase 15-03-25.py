'''
edad = int(input("Introduce tu edad: "))

if edad <= 17:
    print ("Eres menor de edad")
elif edad >=18 and edad <=75:
    print ("Eres un aldulto")
else:
    print ("Te cres Chabelo")
'''

#mientra se mayor de 18 no se ejecuta

edad = 0

while edad < 18:
    
    edad = int(input("Ingrese su edad: "))

    if edad >= 18:
        print ("Eres mayor de edad")
    else:
        print ("Eres menor de edad")
