class Almacenamiento:
    def guardar(self, texto):
        with open("reporte.txt", "w") as f:
            f.write(texto)
        print("Reporte guardado en reporte.txt")
