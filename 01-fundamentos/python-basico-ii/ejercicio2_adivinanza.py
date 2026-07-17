# Ejercicio 2: Juego de adivinanza

import random

numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("Adivina el número entre 1 y 100")

while not adivinado:
    intento = int(input("Tu intento: "))
    intentos += 1
    
    if intento == numero_secreto:
        print(f"¡Ganaste en {intentos} intentos!")
        adivinado = True
    elif intento < numero_secreto:
        print("El número es más grande")
    else:
        print("El número es más pequeño")