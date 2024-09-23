# Inicializaciòn del proceso para crear una aplicaciòn de agenda que nos permita agregar eventos con fechas, horas y descripciòn
# Usamos tkinter para inicializalizar nuestra aplicaciòn.
import tkinter as tk
# Con messagebox podemos implementar cuadreos de mes y advertencias
from tkinter import ttk, messagebox
# Implementamos calendarios
from tkcalendar import DateEntry

# Clase que inicia con nuestra agenda
class Appagenda:
    def __init__(self, root):
        # Formamos la interfàz de nuestra aplicaciòn
        self.root = root
        self.root.title("AGENDA PERSONAL")
        self.root.geometry("600x400")

        # Frame para lista de eventos
        self.lista = tk.Frame(self.root)
        self.lista.pack(fill=tk.BOTH, expand=True)

        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(self.lista, columns=("Fecha", "Hora", "Descripcion"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripcion", text="Descripcion")
        self.tree.column("Fecha", width=100)
        self.tree.column("Hora", width=100)
        self.tree.column("Descripcion", width=300)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Frame para los campos de entrada
        self.entrada = tk.Frame(self.root)
        self.entrada.pack(fill=tk.X)

        # Etiqueta para mostrar "fecha"
        tk.Label(self.entrada, text="Fecha").grid(row=0, column=0, padx=5, pady=5)
        self.fecha = DateEntry(self.entrada, date_pattern='yyyy-mm-dd')
        self.fecha.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta para mostrar "Hora"
        tk.Label(self.entrada, text="Hora").grid(row=1, column=0, padx=5, pady=5)
        self.hora = tk.Entry(self.entrada)
        self.hora.grid(row=1, column=1, padx=5, pady=5)

        # Etiqueta para mostrar "Descripciòn"
        tk.Label(self.entrada, text="Descripcion").grid(row=2, column=0, padx=5, pady=5)
        self.desc = tk.Entry(self.entrada)
        self.desc.grid(row=2, column=1, padx=5, pady=5)

        # Frame para los botones
        self.botones = tk.Frame(self.root)
        self.botones.pack(fill=tk.X)

        # Implementar botòn "Agregar"
        self.bt_agregar = tk.Button(self.botones, text="Agregar Evento", command=self.agregar_evento)
        self.bt_agregar.pack(side=tk.LEFT, padx=5, pady=5)

        # Implementar botòn "Eliminar"
        self.bt_eliminar = tk.Button(self.botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.bt_eliminar.pack(side=tk.LEFT, padx=5, pady=5)

        # Implementar botòn "Salir"
        self.bt_salir = tk.Button(self.botones, text="Salir", command=self.root.quit)
        self.bt_salir.pack(side=tk.RIGHT, padx=5, pady=5)

    # Funciòn para agregar envento
    def agregar_evento(self):
        fecha = self.fecha.get()
        hora = self.hora.get()
        descripcion = self.desc.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.fecha.set_date(None)
            self.hora.delete(0, tk.END)
            self.desc.delete(0, tk.END)
        else:
            messagebox.showwarning("ADVERTENCIA", "Todos los campos son obligatorios")

    # Funciòn para eliminar envento
    def eliminar_evento(self):
        item_selec = self.tree.selection()

        if item_selec:
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar el evento seleccionado?")
            if confirm:
                for item in item_selec:
                    self.tree.delete(item)
        else:
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar")

# Llamamos a la clase para inicializar la aplicaciòn
if __name__ == "__main__":
    root = tk.Tk()
    app = Appagenda(root)
    root.mainloop()
# Fin del proceso
