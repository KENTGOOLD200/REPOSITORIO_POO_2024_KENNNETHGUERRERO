import tkinter as tk
# Convierte a nuestro còdigo en una aplicaciòn
from tkinter import messagebox
# muestra cuadros de informaciòn y advertencias

# Creamos una clace para nuestra aplicaciòn
class GUIApp:
    def __init__(self, app):
        # Metodo para construir nuestra aplicaciòn
        self.app = app
        self.app.title("Gestor de datos")
        # Nombre de nustra app

        # Etiqueta de texto
        self.label = tk.Label(app, text="Ingrese la informaciòn:")
        self.label.pack()

        # Añadir campo de texto
        self.entry = tk.Entry(app)
        self.entry.pack()

        # Llama a comando para agregar texto
        self.agregar_boton_agrgar = tk.Button(text="Agregar", command=self.agregar_datos)
        self.agregar_boton_agrgar.pack()

        # Almacen de entradas
        self.almacen_datos = tk.Listbox(app)
        self.almacen_datos.pack()

        # Limpiar almacèn de datos
        self.boton_limpiar = tk.Button(text="Limpiar", command=self.vaciar_almacen)
        self.boton_limpiar.pack()

        # Salir de la aplicaciòn
        self.salir_final = tk.Button(text="Salir", command=self.salir)
        self.salir_final.pack()

    def agregar_datos(self):
        # Funciòn para agregar datos
        data = self.entry.get()
        if data:
            self.almacen_datos.insert(tk.END, data)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia","Error, el campo està vacìo, intentalo nuevamente por favor.")

    def vaciar_almacen(self):
        # Funciòn para almacenar los datos
        self.almacen_datos.delete(0, tk.END)

    def salir(self):
        # Funciòn para salir de la aplicaciòn
        app.destroy()


if __name__ == "__main__":
    # Ejecutamos la aplicaciòn
    app = tk.Tk()
    aplicacion = GUIApp(app)
    app.mainloop()