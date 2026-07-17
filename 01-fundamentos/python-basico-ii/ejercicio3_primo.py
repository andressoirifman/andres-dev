# Ejercicio 3: Verificar si un número es primo

def es_primo(numero):
    """Retorna True si el número es primo, False si no"""
    if numero < 2:
        return False
    
    for i in range(2, numero):
        if numero % i == 0:
            return False
    
    return True

# Pruebas
numeros = [2, 5, 10, 17, 20, 23]

for num in numeros:
    if es_primo(num):
        print(f"{num} es primo")
    else:
        print(f"{num} NO es primo")