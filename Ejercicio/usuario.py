class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"{self.nombre_usuario} - {self.correo_usuario}"
