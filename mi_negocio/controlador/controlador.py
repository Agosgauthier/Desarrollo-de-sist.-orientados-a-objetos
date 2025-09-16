from modelo.producto import Producto
from estrategia.porcentaje import DescuentoPorcentaje
from estrategia.sin_descuento import SinDescuento

class Controlador:
    def __init__(self, vista):
        self.vista = vista
    
    def elegir_estrategia(self, producto):
        if producto.precio > 150:
            return DescuentoPorcentaje(20)  
        else:
            return SinDescuento()

    def calcular_precio_final(self):
        producto = Producto("Zapatillas", 100)
        
        estrategia = self.elegir_estrategia(producto)

        precio_final = estrategia.aplicar_descuento(producto.precio)
        self.vista.mostrar_precio(producto.nombre, precio_final)
