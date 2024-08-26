# Uso de import para almacenar los productos en un archivo .json
import json
from json import JSONDecodeError

# Clase Producto para representar un producto en el inventario
class Producto:

    def __init__(self, id, nombre, cantidad, precio):
        # Inicializaciòn de los atributos del producto
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        #Devuelve una representaciòn en cadena del producto
        return f"ID del producto:{self.id}, Nombre del producto:{self.nombre}, Cantidad de producto:{self.cantidad}, Precio del producto: ${self.precio}"


# Clase inventario para gestionar una colecciòn de productos
class inventario:

    def __init__(self):
        # Inicializa un dicionario vacìo para almacenar los productos
        self.galeria_produto = {}

    def cargar_inventario(self, info="almacen.json"):
        # Carga el inventario desde un archivo .jason
        try:
            with open(info, "r") as f:
                self.galeria_produto = json.load(f)
        except FileNotFoundError:
            # Maneja el caso en el que el archivo no se encuentra
            print("Documento de almacenamiento no encontrado, se crearà uno nuevo al guardar.")
            self.galeria_produto = {}
        except JSONDecodeError:
            # Maneja el caso de que el archivo se encuentra en formato incorrecto
            print("formato de archivo incorrecto, por favor, verifique el archivo.")
            self.galeria_produto = {}

    def guardar_inventario(self, info="almacen.json"):
        # Guarda el inventario en el archivo .json
        try:
            with open(info, "w") as f:
                json.dump(self.galeria_produto, f, indent=4)
        except Exception as e:
            # Maneja cualquier excepciòn que ocurra en el guardado
            print(f"Error, no se ha podido guardar el producto: {e}")

    def insertar_producto(self, produto):
        # inserta un nuevo producto en el inventario
        if produto.id in self.galeria_produto:
            print("Producto ya existente")
        else:
            self.galeria_produto[produto.id] = produto.__dict__

    def eliminar_producto(self, id):
        # Elimina los productos del inventario por medio de su ID
        if id in self.galeria_produto:
            del self.galeria_produto[id]
            print(f"EL producto {id} ha sido eliminado")
        else:
            print("Error, el producto no existe")

    def actualizar_producto(self, id, cantidad= None, precio= None):
        # Actualiza la cantidad y el precio del producto por medio de su ID
        if id in self.galeria_produto:
            if cantidad is not None:
                self.galeria_produto[id]["cantidad"]= cantidad
            if precio is not None:
                self.galeria_produto[id]["precio"]= precio
            print(f"El producto {id} ha sido actualizado")
        else:
            print("Producto inexistente")

    def imprimir_inventario(self):
        # Imprime todos los produtos del inventario
        if not self.galeria_produto:
            print("Sin produtos en el inventario")
        else:
            for id, informacion in self.galeria_produto.items():
                try:
                    item = Producto(id, informacion["nombre"], informacion["cantidad"], informacion["precio"])
                    print(item)
                except KeyError as e:
                    print(f"Error, el produto no se puede mostrar porque està incompleto, falta el campo{e}")


# Funciòn para mostrar todas las opciones del inventario
def menu():
    print("Bienvenidos al sistema de control de inventario de la tienda")
    Inventario = inventario()
    Inventario.cargar_inventario()
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto por ID")
        print("4. Mostrar inventario")
        print("5. Guardar y salir del proceso")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Añadir un nuevo producto
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = input("Ingrese la cantidad del producto: ")
            precio = input("Ingrese el precio del producto: ")
            pro = Producto(id, nombre, cantidad, precio)
            Inventario.insertar_producto(pro)
            Inventario.guardar_inventario()
            print("Producto añadido con éxito.")

        elif opcion == '2':
            # Eliminar un producto por su ID
            id = input("Ingrese el id del procuto que desea eliminar")
            Inventario.eliminar_producto(id)
            Inventario.guardar_inventario()

        elif opcion == '3':
            # Actualizar cantidad o precio de un producto por ID
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiarla): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            Inventario.actualizar_producto(id, cantidad, precio)
            Inventario.guardar_inventario()

        elif opcion == '4':
            # Imprime todos los productos del inventario
            Inventario.imprimir_inventario()

        elif opcion == '5':
            # Guardar el inventario y salir del programa
            Inventario.guardar_inventario()
            print("Inventario guardado correctamente. Saliendo..")
            break
        else:
            print("Ocurriò un error inesperado al realizar el proceso")

# Poner el còdigo en marcha
if __name__== "__main__":
    menu()