
frase = input("Ingresa una frase: ")

palabras = frase.split()

contador = 0
    
for palabra in palabras:
    contador += 1
    
print(f"La frase tiene {contador} palabras.")