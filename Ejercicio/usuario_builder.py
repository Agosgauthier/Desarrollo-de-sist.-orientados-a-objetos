from usuario import Usuario

# Builder para crear usuarios con nombres de métodos más simples
class UsuarioBuilder:
    def __init__(self):
        self.nombre_usuario = ""
        self.correo_usuario = ""

    def nombre(self, valor):
        self.nombre_usuario = valor
        return self

    def correo(self, valor):
        self.correo_usuario = valor
        return self

    def construir(self):
        return Usuario(self.nombre, self.correo)