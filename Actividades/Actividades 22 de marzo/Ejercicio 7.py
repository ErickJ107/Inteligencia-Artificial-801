op = input("Elige una operacion (+, -, *, /): ")
a = int(input("Primer número: "))
b = int(input("Segundo número: "))

match op:
    case "+":
        print ("Resultado:", a + b)
    case "-":
        print ("Resultado:", a - b)
    case "*":
        print ("Resultado:", a * b)
    case "/":
        print ("Resultado:", a / b if b != 0 else "No se puede dividir entre cero")
    case _:
        print ("Operación invalida.")