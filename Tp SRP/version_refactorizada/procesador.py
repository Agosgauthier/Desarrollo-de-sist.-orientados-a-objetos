class Procesador:
    def calcular_promedio(self, datos):
        if not datos:
            return 0
        return sum(datos) / len(datos)
