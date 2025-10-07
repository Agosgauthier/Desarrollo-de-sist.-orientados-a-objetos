class Reporte:
    def __init__(self):
        self.datos = []

    def obtener_datos(self):
        self.datos = [10, 20, 30, 40, 50]

    def procesar_datos(self):
        if not self.datos:
            return 0
        return sum(self.datos) / len(self.datos)

    def generar_texto(self, promedio):
        return f"El promedio de los datos es: {promedio}"
    
    def guardar_reporte(self, texto):
        with open("reporte.txt", "w") as f:
            f.write(texto)
        print("Reporte guardado en reporte.txt")

    def ejecutar(self):
        self.obtener_datos()
        promedio = self.procesar_datos()
        texto = self.generar_texto(promedio)
        self.guardar_reporte(texto)
        print("Proceso completo.")


if __name__ == "__main__":
    reporte = Reporte()
    reporte.ejecutar()