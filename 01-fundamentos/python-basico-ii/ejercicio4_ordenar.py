# Ejercicio 4: Ordenar una lista sin usar sorted()

def ordenar_lista(lista):
    """Ordena una lista de menor a mayor (sin usar sorted())"""
    nueva_lista = lista.copy()  # Copiar para no modificar la original
    
    for i in range(len(nueva_lista)):
        for j in range(i + 1, len(nueva_lista)):
            if nueva_lista[i] > nueva_lista[j]:
                # Intercambiar elementos
                nueva_lista[i], nueva_lista[j] = nueva_lista[j], nueva_lista[i]
    
    return nueva_lista

# Pruebas
numeros = [5, 2, 8, 1, 9, 3]
print(f"Lista original: {numeros}")
print(f"Lista ordenada: {ordenar_lista(numeros)}")