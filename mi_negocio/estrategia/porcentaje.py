from estrategia.base import EstrategiaDescuento

class DescuentoPorcentaje(EstrategiaDescuento):
    def __init__(self, porcentaje):
        self.porcentaje = porcentaje

    def aplicar_descuento(self, precio):
        return precio * (1 - self.porcentaje / 100)
