import random

chistes = [
    "El otro día vendí mi aspiradora. Lo único que hacía era acumular polvo.",
    "¿Qué es rojo y tiene forma de cubo? Un cubo azul pintado de rojo.",
    "¿Qué le dice un jardinero a otro? Nos vemos cuando podamos.",
    "Había un tipo que era tan borrachín que le llamaban 'genio' porque cada vez que destapaban una botella aparecía.",
    "Te iba a contar un chiste sobre el aborto, pero no me nacio",
    "¿Qué le dijo Batman a Robin antes de subir al coche? 'Robin, sube al coche'.",
    "¿Has oído hablar del astronauta claustrofóbico? Solo necesitaba un poco de espacio.",
    "¿Cómo se despiden los químicos? Ácido un placer.",
    "¿Cómo se llama el campeón de buceo japonés? Tokofondo.",
    "Iba a contar un chiste sobre sodio... pero Na.",
    "- ¡Capitán, capitán! Están a punto de atacarnos 40 carabelas.    - ¿Una flota?    - No, flotan todas."
]

user = str(input(""))

if user == "Cuentame un chiste":
    print (random.choice(chistes))
else:
    print ("Error")