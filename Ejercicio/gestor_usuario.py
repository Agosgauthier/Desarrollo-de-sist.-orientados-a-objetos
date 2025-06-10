from usuario import Usuario

# Singleton para gestionar usuarios (sin __new__)
class GestorUsuarios:
    instancia = None

    def __init__(self):
        if not GestorUsuarios.instancia:
            GestorUsuarios.instancia = self
            self.usuarios = []

    def agregar(self, usuario):
        self.usuarios.append(usuario)