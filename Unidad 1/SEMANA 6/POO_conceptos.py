# Inicializacion del proceso para repasar los conceptos de POO

#clase madre
class animal:
    def __init__(self, name): # Definición de métodos de clase animal
        self.name = name

    def speak(self): # Metodo que simula el sonido de los humanos
        pass

# Clase hija 1
class Dog(animal):
    def speak(self):
        return f"{self.name} dice '¡Guau!'" # Hacemos uso del método speak para simular el sonido del perro

# Clase hija 2
class Cat(animal):
    def speak(self):
        return f"{self.name} dice '¡Miau!'" # Hacemos uso del método speak para simular el sonido del gato.


# LLamamos a los métodos para imprimir los resultados.
if __name__ == "__main__":
    # Creación de instancias
    perro = Dog("Firulais")
    gato = Cat("Garfield")

    # Llamada a los métodos
    print(perro.speak())
    print(gato.speak())