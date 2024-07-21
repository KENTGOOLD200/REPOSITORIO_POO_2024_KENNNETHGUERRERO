# Se requiere un programa que calcule el aumento de sueldo de los trabajadores de una empresa, segun sus años de servicio.
# Inicialización del proceso
# Definición de la clase, en este caso, la clase será "Trabajadores"
class trabajadores:

    # Definición del método para pedir los datos del empleado siguiendo la convención snake_case
    def __init__(self):
        # Definición de los atributos
        # Utilización de datos string como parte de este atributo
        self.nombre = input("Ingrese el nombre del trabajador, por ejemplo (Marco Díaz): ")
        # Utilización de datos integer como parte de este atributo
        self.edad = int(input("Ingrese la edad del trabajador, por ejemplo (30): "))
        # Utilización de datos string como parte de este atributo
        self.cargo = input("Ingrese el cargo del trabajador, por ejemplo (Director de Marketing): ")
        # Utilización de datos float como parte de este atributo
        self.salario = float(input("Ingrese el salario del trabajador, por ejemplo (550.20): "))
        # Utilización de datos integer como parte de este atributo
        self.tiempo_servicio = int(input("Ingrese el número de años de servicio del trabajador hacia la empresa: "))
        self.nuevo_salario = 0

    # Definición del método para calcular el porcentaje de aumento de sueldo del empleado siguiendo la convención snake_case
    def calculo_aumento(self):
        # Utilización de datos boolean, haciendo uso de la condicional if-else
        if self.tiempo_servicio >= 3 and self.tiempo_servicio < 6:
            self.nuevo_salario = self.salario / 100 * 15
            #Imprimir resultados
            print("El salario del trabajador",self.nombre,"aumentó un 15%, ahora la remuneración será de: ", self.nuevo_salario + self.salario)
        elif self.tiempo_servicio >= 6 and self.tiempo_servicio < 10:
            self.nuevo_salario = self.salario / 100 * 30
            # Imprimir resultados
            print("El salario del trabajador",self.nombre,"aumentó un 30%, ahora la remuneración será de: ", self.nuevo_salario + self.salario)
        elif self.tiempo_servicio >= 10:
            self.nuevo_salario = self.salario / 100 * 50
            # Imprimir resultados
            print("El salario del trabajador",self.nombre,"aumentó un 50%, ahora la remuneración será de: ", self.nuevo_salario + self.salario)
        else:
            # Imprimir un mensaje de error por si no se da un dato válido para un aumento de sueldo
            print("Lo lamentamos,el trabajador",self.nombre,"aún no úede tener el beneficio de un aumento")

# Mensaje decorativo para dar contexto del proceso
print("¡BIENVENIDO AL SISTEMA DE CALCULO DE AUMENTO DE SALARIOS DE LA EMPRESA (IMPORTADORA CRIS/KEN)")
# Definición del objeto, llamando a los métodos de su clase siguiendo la convención snake_case
empleado_empresa = trabajadores()
empleado_empresa.calculo_aumento()