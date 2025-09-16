from estrategia.base import EstrategiaDescuento

class SinDescuento(EstrategiaDescuento):
    def aplicar_descuento(self, precio):
        return precio
