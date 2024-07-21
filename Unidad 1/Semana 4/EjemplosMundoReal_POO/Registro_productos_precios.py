#EN UNA TIENDA DE ROPA SE REQUIERE UN PROGRAMA PARA REGISTRAR LA NUEVA MERCADERÍA QUE ENTRA A LA MISMA, SABER SU TALLA, MARCA, COLOR Y PRECIOS

#INICIALIZACIÓN DEL ALGORITMO
#DEFINICIÓN DE LAS CLASES, EN ESTE CASO LA CLASE SERÁ "PRENDA"
class Prenda:

    #DEFINICIÓN DE LOS MÉTODOS
    def __init__(self):

        #DEFINICIÓN DE LOS ATRIBUTOS
        self.talla = input("Ingrese la talla de la prenda: ")
        self.color = input("Ingrese el color de la prenda: ")
        self.marca = input("Ingrese la marca de la prenda: ")
        self.precio = input("Ingrese el precio de la prenda: ")

#DECLARACIÓN DE OBJETOS
objeto_ropa = input("Ingrese en mayúsculas el tipo de prenda que desea añadir (CAMISA, PANTALON, CHAQUETA): ") #IMPLEMENTACIÓN DE UNA VARIABLE QUE NOS PERMITA DEFINIR LOS OBJETOS

#IMPLEMENTACIÓN DE LA CONDICIONAL IF-ELSE PARA ELEGIR EL OBJETO DESEADO
if objeto_ropa == "CAMISA":
    #OBJETO UNO
    camisa = Prenda()
    #IMPRIMIR RESULTADOS
    print(camisa.talla, camisa.color, camisa.marca, camisa.precio)
    print("LA PRENDA", objeto_ropa, "SE HA AÑADIDO CORRECTAMENTE.")
elif objeto_ropa == "PANTALON":
    #OBJETO DOS
    pantalon = Prenda()
    #IMPRIMIR RESULTADOS
    print(pantalon.talla, pantalon.color, pantalon.marca, pantalon.precio)
    print("LA PRENDA", objeto_ropa, "SE HA AÑADIDO CORRECTAMENTE.")
elif objeto_ropa == "CHAQUETA":
    #OBJETO TRES
    chaqueta = Prenda()
    # IMPRIMIR RESULTADOS
    print(chaqueta.talla, chaqueta.color, chaqueta.marca, chaqueta.precio)
    print("LA PRENDA", objeto_ropa, "SE HA AÑADIDO CORRECTAMENTE.")
else:
    #MENSAJE DE ERROR POR SI SE ELIJE UN OBJETO NO EXISTENTE
    print("Error, caracter no admitido.")
#FINALIZACIÓN DEL ALGORITMO