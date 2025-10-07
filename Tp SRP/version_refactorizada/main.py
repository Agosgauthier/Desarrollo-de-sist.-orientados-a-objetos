from fuente_datos import FuenteDatos
from procesador import Procesador
from generador_reporte import GeneradorReporte
from almacenamiento import Almacenamiento

class Main:
    def ejecutar(self):
        fuente = FuenteDatos()
        procesador = Procesador()
        generador = GeneradorReporte()
        almacenamiento = almacenamiento()

        datos = fuente.obtener()
        promedio = procesador.calcular_promedio(datos)
        texto = generador.crear(promedio)
        almacenamiento.guardar(texto)
        print(texto)
        print("Proceso completo.")


if __name__ == "__main__":
    app = Main()
    app.ejecutar()

