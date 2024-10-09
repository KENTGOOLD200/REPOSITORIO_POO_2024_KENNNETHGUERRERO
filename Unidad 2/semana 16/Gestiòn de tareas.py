# Creaciòn de una app de gestiòn de tareas que permita agregar tareas, marcar como copletada (tecla enter), eliminar tarea (tecla ') y cerrar la aplicaciòn (tecla escape)
import tkinter as tk
from tkinter import messagebox

# Clase principal para la gestión de tareas
class TaskManager:
    def __init__(self, root):
        # Inicialización de la ventana principal
        self.root = root
        self.root.title("Gestión de Tareas")
        self.tasks = []  # Lista para almacenar las tareas

        # Campo de entrada para añadir nuevas tareas
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        # Vincula la tecla "Enter" para añadir tareas
        self.entry.bind("<Return>", self.add_task)

        # Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Botón para añadir tareas
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Botón para marcar tareas como completadas
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Botón para eliminar tareas
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Vincula la tecla "Enter" para marcar tareas como completadas
        self.root.bind("<Return>", lambda event: self.complete_task())
        # Vincula la tecla "'" para eliminar tareas
        self.root.bind("<'>", lambda event: self.delete_task())
        # Vincula la tecla "Escape" para cerrar la aplicación
        self.root.bind("<Escape>", lambda event: root.quit())

    # Función para añadir una nueva tarea
    def add_task(self, event=None):
        task = self.entry.get()  # Obtiene el texto del campo de entrada
        if task:  # Verifica que no esté vacío
            self.tasks.append(task)  # Añade la tarea a la lista
            self.update_task_listbox()  # Actualiza la lista de tareas en la interfaz
            self.entry.delete(0, tk.END)  # Limpia el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")  # Muestra un mensaje de advertencia

    # Función para marcar una tarea como completada
    def complete_task(self, event=None):
        selected_task_index = self.task_listbox.curselection()  # Obtiene el índice de la tarea seleccionada
        if selected_task_index:  # Verifica que haya una tarea seleccionada
            task = self.tasks[selected_task_index[0]]  # Obtiene la tarea de la lista
            self.tasks[selected_task_index[0]] = f"{task} (Completada)"  # Marca la tarea como completada
            self.update_task_listbox()  # Actualiza la lista de tareas en la interfaz
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para completar.")  # Muestra un mensaje de advertencia

    # Función para eliminar una tarea
    def delete_task(self, event=None):
        selected_task_index = self.task_listbox.curselection()  # Obtiene el índice de la tarea seleccionada
        if selected_task_index:  # Verifica que haya una tarea seleccionada
            del self.tasks[selected_task_index[0]]  # Elimina la tarea de la lista
            self.update_task_listbox()  # Actualiza la lista de tareas en la interfaz
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")  # Muestra un mensaje de advertencia

    # Función para actualizar la lista de tareas en la interfaz
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Limpia la lista de tareas en la interfaz
        for task in self.tasks:  # Añade cada tarea a la lista de tareas en la interfaz
            self.task_listbox.insert(tk.END, task)

# Código principal para ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = TaskManager(root)  # Crea una instancia de la clase TaskManager
    root.mainloop()  # Inicia el bucle principal de la aplicación
