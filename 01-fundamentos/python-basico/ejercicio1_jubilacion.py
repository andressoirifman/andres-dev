# Ejercicio 1: Calcular años hasta jubilación

edad_actual = int(input("¿Cuántos años tienes? "))
jubilacion = 65
años_restantes = jubilacion - edad_actual

if años_restantes > 0:
    print(f"Te faltan {años_restantes} años para jubilarte")
elif años_restantes == 0:
    print("¡Ya alcanzaste la edad de jubilación!")
else:
    print(f"¡Pasaste la edad de jubilación hace {años_restantes * -1} años!")