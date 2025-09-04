from vista.vista import Vista
from controlador.controlador import Controlador

if __name__ == "__main__":
    vista = Vista()
    controlador = Controlador(vista)
    controlador.calcular_precio_final()
