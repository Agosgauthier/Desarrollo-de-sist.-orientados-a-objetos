from usuario import Usuario

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

    def build(self):
        return Usuario(self.nombre_usuario, self.correo_usuario)
