from modelos.usuario import Usuario

class UsuarioBuilder:
    def __init__(self):
        self.nombre = ""
        self.clave = ""

    def con_nombre(self, nombre):
        self.nombre = nombre
        return self

    def con_clave(self, clave):
        self.clave = clave
        return self

    def construir(self):
        return Usuario(self.nombre, self.clave)

