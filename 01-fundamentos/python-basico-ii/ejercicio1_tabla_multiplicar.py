# Ejercicio 1: Tabla de multiplicar

numero = int(input("¿De qué número quieres la tabla? "))

print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")