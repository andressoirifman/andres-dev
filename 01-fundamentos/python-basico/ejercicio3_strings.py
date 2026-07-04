# Ejercicio 3: Manipular strings

palabra = input("Escribe una palabra: ")

# Invertir
invertida = palabra[::-1]

# Contar vocales
vocales = "aeiouAEIOU"
contador_vocales = sum(1 for letra in palabra if letra in vocales)

print(f"Palabra original: {palabra}")
print(f"Palabra invertida: {invertida}")
print(f"Vocales: {contador_vocales}")