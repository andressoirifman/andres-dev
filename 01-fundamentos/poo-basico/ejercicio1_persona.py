# Ejercicio 1: Clase Persona

class Persona:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email
    
    def saludar(self):
        print(f"Hola, me llamo {self.nombre}")
    
    def calcular_edad_jubilacion(self):
        años_restantes = 65 - self.edad
        if años_restantes > 0:
            print(f"{self.nombre} se jubila en {años_restantes} años")
        else:
            print(f"{self.nombre} ya se jubilo hace {años_restantes * -1} años")

# Pruebas
persona1 = Persona("Andrés", 30, "andres@gmail.com")
persona1.saludar()
persona1.calcular_edad_jubilacion()

persona2 = Persona("María", 45, "maria@gmail.com")
persona2.saludar()
persona2.calcular_edad_jubilacion()