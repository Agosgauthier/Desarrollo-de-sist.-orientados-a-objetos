# Servicio de login con DI (recibe la estrategia como parámetro)
class ServicioLogin:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def login(self, usuario):
        if self.estrategia.autenticar(usuario):
            print("Login exitoso")
        else:
            print("Usuario o contraseña incorrectos")
