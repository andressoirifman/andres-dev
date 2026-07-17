# Ejercicio 2: Clase Producto

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}")
        else:
            print(f"Stock insuficiente. Disponible: {self.stock}")
    
    def reponer(self, cantidad):
        self.stock += cantidad
        print(f"Se agregaron {cantidad} unidades. Stock total: {self.stock}")

# Pruebas
producto1 = Producto("Laptop", 1000, 5)
print(f"Stock inicial: {producto1.stock}")

producto1.vender(2)
print(f"Stock después de venta: {producto1.stock}")

producto1.reponer(3)
print(f"Stock después de reposición: {producto1.stock}")

producto1.vender(10)  # Intenta vender más de lo disponible