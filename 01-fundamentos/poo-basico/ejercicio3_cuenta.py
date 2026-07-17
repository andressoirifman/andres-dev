# Ejercicio 3: Clase Cuenta

class Cuenta:
    def __init__(self, propietario, saldo_inicial=0):
        self.propietario = propietario
        self.saldo = saldo_inicial
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de ${cantidad} realizado. Saldo actual: ${self.saldo}")
        else:
            print("La cantidad debe ser mayor a cero")
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print(f"Saldo insuficiente. Disponible: ${self.saldo}")
        elif cantidad > 0:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado. Saldo actual: ${self.saldo}")
        else:
            print("La cantidad debe ser mayor a cero")

# Pruebas
cuenta = Cuenta("Juan", 1000)
print(f"Saldo inicial: ${cuenta.saldo}")

cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(2000)  # Intenta retirar más de lo disponible