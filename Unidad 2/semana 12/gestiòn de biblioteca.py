# Clase Libro para representar un libro en la biblioteca
class Libro:
    def __init__(self, isbn, titulo, autor, categoria):
        # Inicializa los atributos del libro
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria

    def __str__(self):
        # Devuelve una representación en cadena del libro
        return f"ISBN: {self.isbn}, Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}"

# Clase Usuario para representar un usuario de la biblioteca
class Usuario:
    def __init__(self, id_usuario, nombre):
        # Inicializa los atributos del usuario
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []

    def __str__(self):
        # Devuelve una representación en cadena del usuario
        return f"ID Usuario: {self.id_usuario}, Nombre: {self.nombre}, Libros Prestados: {[libro.titulo for libro in self.libros_prestados]}"

# Clase Biblioteca para gestionar la colección de libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        # Inicializa los diccionarios para libros disponibles y usuarios registrados
        self.libros_disponibles = {}
        self.usuarios_registrados = {}

    def sumar_libro(self, libro):
        # Añade un libro a la biblioteca si no existe ya
        if libro.isbn in self.libros_disponibles:
            print("El libro ya existe en la biblioteca.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido con éxito.")

    def eliminar_libro(self, isbn):
        # Elimina un libro de la biblioteca si existe
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado con éxito.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        # Registra un nuevo usuario en la biblioteca si no está ya registrado
        if usuario.id_usuario in self.usuarios_registrados:
            print("El usuario ya está registrado.")
        else:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")

    def dar_de_baja_usuario(self, id_usuario):
        # Da de baja a un usuario de la biblioteca si está registrado
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja con éxito.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        # Presta un libro a un usuario registrado si el libro está disponible
        if id_usuario not in self.usuarios_registrados:
            print("El usuario no está registrado.")
            return
        if isbn not in self.libros_disponibles:
            print("El libro no está disponible.")
            return

        libro = self.libros_disponibles.pop(isbn)
        usuario = self.usuarios_registrados[id_usuario]
        usuario.libros_prestados.append(libro)
        print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}' con éxito.")

    def devolver_libro(self, id_usuario, isbn):
        # Permite a un usuario registrado devolver un libro prestado
        if id_usuario not in self.usuarios_registrados:
            print("El usuario no está registrado.")
            return

        usuario = self.usuarios_registrados[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print(f"Libro '{libro.titulo}' devuelto con éxito.")
                return
        print("El libro no fue encontrado en los préstamos del usuario.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        # Busca libros en la biblioteca según el título, autor o categoría
        resultados = []
        for libro in self.libros_disponibles.values():
            if (titulo and titulo in libro.titulo) or (autor and autor in libro.autor) or (categoria and categoria in libro.categoria):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        # Lista los libros prestados por un usuario registrado
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            return usuario.libros_prestados
        return []

def mostrar_menu():
    # Muestra el menú de opciones de la biblioteca virtual
    print("\n--- Menú Biblioteca Virtual ---")
    print("Selecciona una opciòn:")
    print("1. Añadir libro")
    print("2. Eliminar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados")
    print("9. Salir")

def main():
    # Función principal para ejecutar el sistema de la biblioteca
    biblioteca = Biblioteca()

    while True:
        # Bucle para ejecutar el sistema
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Añadir un libro a la biblioteca
            isbn = input("Ingrese ISBN del libro: ")
            titulo = input("Ingrese título del libro: ")
            autor = input("Ingrese autor del libro: ")
            categoria = input("Ingrese categoría del libro: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.sumar_libro(libro)

        elif opcion == "2":
            # Eliminar un libro de la biblioteca
            isbn = input("Ingrese ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)

        elif opcion == "3":
            # Registrar un nuevo usuario en la biblioteca
            id_usuario = input("Ingrese ID del usuario: ")
            nombre = input("Ingrese nombre del usuario: ")
            usuario = Usuario(id_usuario, nombre)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            # Dar de baja a un usuario de la biblioteca
            id_usuario = input("Ingrese ID del usuario a dar de baja: ")
            biblioteca.dar_de_baja_usuario(id_usuario)

        elif opcion == "5":
            # Prestar un libro a un usuario registrado
            id_usuario = input("Ingrese ID del usuario: ")
            isbn = input("Ingrese ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            # Devolver un libro prestado por un usuario registrado
            id_usuario = input("Ingrese ID del usuario: ")
            isbn = input("Ingrese ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            # Buscar libros en la biblioteca
            titulo = input("Ingrese título del libro (opcional): ")
            autor = input("Ingrese autor del libro (opcional): ")
            categoria = input("Ingrese categoría del libro (opcional): ")
            resultados = biblioteca.buscar_libro(titulo, autor, categoria)
            if resultados:
                print("Libros encontrados:")
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros.")

        elif opcion == "8":
            # Listar los libros prestados por un usuario registrado
            id_usuario = input("Ingrese ID del usuario: ")
            libros_prestados = biblioteca.listar_libros_prestados(id_usuario)
            if libros_prestados:
                print("Libros prestados:")
                for libro in libros_prestados:
                    print(libro)
            else:
                print("No hay libros prestados.")

        elif opcion == "9":
            # Salir del sistema
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

