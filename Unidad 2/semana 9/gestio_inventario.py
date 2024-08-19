# Inicialización de un proceso para simular un control de inventario para una tienda

# Clase que representa un producto en el inventario
class Producto:
    def __init__(self,id, nombre, cantidad, precio):
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
    def set_id (self, id):
        self.id = id
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    def set_precio(self, precio):
        self.precio = precio

# Clase que maneja el inventario de productos
class Inventario:
    def __init__(self):
        # Inicializa una lista vacía para almacenar los productos
        self.lista_producto = []

        # Método para agregar un producto al inventario
    def agregar_produto(self, producto):
        self.lista_producto.append(producto)

    # Método para eliminar un producto del inventario por medio de su ID
    def eliminar_producto (self, id):
        for producto in self.lista_producto:
            if producto.get_id() == id:
                self.lista_producto.remove(producto)
            break

    # Método para actualizar la cantidad o el precio de un producto por su ID
    def actualizar_producto(self, id, cantidad = None, precio = None):
        for producto in self.lista_producto:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                break

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
            inventario.agregar_produto(producto)
            print("Producto añadido con éxito.")

        elif opcion == '2':
            # Eliminar un producto por ID
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
            print("Producto eliminado con éxito.")

        elif opcion == '3':
            # Actualizar cantidad o precio de un producto por ID
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiarla): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
            print("Producto actualizado con éxito.")

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
