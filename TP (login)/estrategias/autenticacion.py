class EstrategiaAutenticacion:
    def autenticar(self, usuario):
        raise NotImplementedError()

class AutenticacionSimple(EstrategiaAutenticacion):
    def __init__(self):
        self.usuario_valido = "agoss"
        self.clave_valida = "1234"

    def autenticar(self, usuario):
        return usuario.nombre == self.usuario_valido and usuario.clave == self.clave_valida

