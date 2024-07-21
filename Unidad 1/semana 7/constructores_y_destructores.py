# Inicialización de un proceso de experimentación usando métodos contsructores y destructores en un programa en Python

# Experimentación usando métodos constructores y destructores clásicos
# Declaración de la clase electrodomestico
class electrodomestico():
    # Método constructor (__init__) que inicializa los atributos del objeto
    def __init__(self, tipo, marca, color, funcion, electrico, manual):
        self.tipo = f"TIPO = {tipo}"
        self.marca = f"MARCA = {marca}"
        self.color = f"COLOR = {color}"
        self.funcion = f"FUNCIÓN = {funcion}"
        self.electrico = f"ELECTRICO = {electrico}"
        self.manual = f"MANUAL = {manual}"

    # Método destructor (__del__) que se llama cuando el objeto es eliminado
    def __del__ (self):
        print("El objeto ha sido eliminado.")

# Creación de una instancia de la clase electrodomestico
cocina = electrodomestico("COCINA","INDURAMA", "GRIS", "COCER ALIMENTOS", False, True)
# Impresión de los atributos del objeto cocina
print(cocina.tipo)
print(cocina.marca)
print(cocina.color)
print(cocina.funcion)
print(cocina.electrico)
print(cocina.manual)
# Eliminación del objeto cocina
del cocina

# Experimentación con un método para imposibilitar volver a usar un objeto utilizando return None
# Declaración de la clase herramienta
class herramienta():
    # Método constructor (__init__) que inicializa los atributos del objeto
    def __init__(self, tipo, marca, color, funcion, electrico, manual):
        self.tipo = f"\n\nTIPO = {tipo}"
        self.marca = f"MARCA = {marca}"
        self.color = f"COLOR = {color}"
        self.funcion = f"FUNCIÓN = {funcion}"
        self.electrico = f"ELECTRICO = {electrico}"
        self.manual = f"MANUAL = {manual}"

    # Método eliminar que imprime un mensaje y return None
    def eliminar(self):
        print("El objeto ha sido eliminado.")
        return None

# Creación de una instancia de la clase herramienta
taladro = herramienta("TALADRO", "DAEWO", "AMARILLO", "TALADRAR", True, False)
# Impresión de los atributos del objeto taladro
print(taladro.tipo)
print(taladro.marca)
print(taladro.color)
print(taladro.funcion)
print(taladro.electrico)
print(taladro.manual)

# Llamada al método eliminar del objeto taladro
taladro.eliminar()

# Experimentación con el método destructor para eliminar un atributo de un objeto
# Declaración de la clase auto
class auto():
    # Método constructor (__init__) que inicializa los atributos del objeto
    def __init__(self, tipo, marca, color, funcion, electrico, manual):
        self.tipo = f"\n\nMODELO = {tipo}"
        self.marca = f"MARCA = {marca}"
        self.color = f"COLOR = {color}"
        self.funcion = f"FUNCIÓN = {funcion}"
        self.electrico = f"ELECTRICO = {electrico}"
        self.manual = f"MANUAL = {manual}"

    # Método eliminar_atributo que elimina el atributo 'manual' del objeto
    def eliminar_atributo(self):
        delattr(self, "manual")
        print("El atributo 'manual' ha sido eliminado")

# Creación de una instancia de la clase auto
mi_auto = auto("RAPTOR", "FORD", "ROJO", "TRANSPORTAR", True, False)
# Impresión de los atributos del objeto mi_auto
print(mi_auto.tipo)
print(mi_auto.marca)
print(mi_auto.color)
print(mi_auto.funcion)
print(mi_auto.electrico)
print(mi_auto.manual)

# Llamada al método eliminar_atributo del objeto mi_auto
mi_auto.eliminar_atributo()
# Finalización del proceso.