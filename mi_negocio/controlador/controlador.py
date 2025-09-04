from modelo.producto import Producto
from estrategia.porcentaje import DescuentoPorcentaje

class Controlador:
    def __init__(self, vista):
        self.vista = vista

    def calcular_precio_final(self):
        producto = Producto("Zapatillas", 100)
        estrategia = DescuentoPorcentaje(20)
        precio_final = estrategia.aplicar_descuento(producto.precio)
        self.vista.mostrar_precio(producto.nombre, precio_final)
