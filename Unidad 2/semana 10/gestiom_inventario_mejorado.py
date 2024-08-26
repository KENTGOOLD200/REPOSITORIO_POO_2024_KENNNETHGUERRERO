import os

# Clase que representa un producto en el inventario
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Inicializa los atributos del producto
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para obtener los valores de los atributos
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos para establecer nuevos valores a los atributos
    def set_id(self, id):
        self.id = id

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Método para convertir el objeto Producto a una cadena de texto
    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"

    # Método estático para crear un objeto Producto a partir de una cadena de texto
    @staticmethod
    def from_string(producto_str):
        id, nombre, cantidad, precio = producto_str.strip().split(',')
        return Producto(id, nombre, int(cantidad), float(precio))

# Clase que maneja el inventario de productos
class Inventario:
    def __init__(self, archivo='inventario.txt'):
        # Inicializa una lista vacía para almacenar los productos
        self.lista_producto = []
        # Nombre del archivo donde se almacenará el inventario
        self.archivo = archivo
        # Verifica la existencia y permisos del archivo
        self.verificar_archivo()
        # Carga el inventario desde el archivo al iniciar
        self.cargar_inventario()

    # Método para verificar la existencia y permisos del archivo
    def verificar_archivo(self):
        # Verifica si el archivo existe, si no, lo crea
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w') as file:
                pass
        # Verifica los permisos del archivo
        if not os.access(self.archivo, os.R_OK | os.W_OK):
            raise PermissionError(f"No se tienen permisos de lectura/escritura para el archivo {self.archivo}")

    # Método para cargar el inventario desde un archivo
    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    producto = Producto.from_string(linea)
                    self.lista_producto.append(producto)
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    # Método para guardar el inventario en un archivo
    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.lista_producto:
                    file.write(str(producto) + '\n')
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Permiso denegado para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    # Método para agregar un producto al inventario
    def agregar_producto(self, producto):
        self.lista_producto.append(producto)
        # Guarda el inventario actualizado en el archivo
        self.guardar_inventario()

    # Método para eliminar un producto del inventario por medio de su ID
    def eliminar_producto(self, id):
        for producto in self.lista_producto:
            if producto.get_id() == id:
                self.lista_producto.remove(producto)
                # Guarda el inventario actualizado en el archivo
                self.guardar_inventario()
                print("Producto eliminado con éxito.")
                return
        print("Producto no encontrado.")

    # Método para actualizar la cantidad o el precio de un producto por su ID
    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.lista_producto:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                # Guarda el inventario actualizado en el archivo
                self.guardar_inventario()
                print("Producto actualizado con éxito.")
                return
        print("Producto no encontrado.")

    # Método para buscar productos por nombre
    def buscar_producto(self, nombre):
        producto_ubicado = []
        for producto in self.lista_producto:
            if nombre.lower() in producto.get_nombre().lower():
                producto_ubicado.append(producto)
        return producto_ubicado

    # Método para mostrar todos los productos en el inventario
    def mostrar_inventario(self):
        for producto in self.lista_producto:
            print(f"\n\nID del producto: {producto.get_id()}, \nNombre del producto: {producto.get_nombre()}, "f"\nCantidad del producto: {producto.get_cantidad()}, \nPrecio del producto: {producto.get_precio()}")

# Función principal que muestra el menú y maneja las opciones del usuario
def menu():
    print("Bienvenidos al sistema de control de inventario de la tienda")
    inventario = Inventario()
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto por ID")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos en el inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Añadir un nuevo producto
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            print("Producto añadido con éxito.")

        elif opcion == '2':
            # Eliminar un producto por ID
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            # Actualizar cantidad o precio de un producto por ID
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiarla): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            # Buscar productos por nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            productos = inventario.buscar_producto(nombre)
            if productos:
                for producto in productos:
                    print(f"ID del producto: {producto.get_id()}, Nombre del producto: {producto.get_nombre()}, "
                          f"Cantidad del producto: {producto.get_cantidad()}, Precio del producto: {producto.get_precio()}")
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            # Mostrar todos los productos en el inventario
            inventario.mostrar_inventario()

        elif opcion == '6':
            # Salir del menú
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")
if __name__ == "__main__":
    menu()
# Fin del proceso
