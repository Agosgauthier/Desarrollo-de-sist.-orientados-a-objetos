from builders.usuario_builder import UsuarioBuilder
from estrategias.autenticacion import AutenticacionSimple
from servicios.login import ServicioLogin

# Punto de entrada
if __name__ == "__main__":
    nombre = input("Ingrese su nombre de usuario: ")
    clave = input("Ingrese su contraseña: ")

    usuario = UsuarioBuilder().con_nombre(nombre).con_clave(clave).construir()
    estrategia = AutenticacionSimple()
    servicio = ServicioLogin(estrategia)

    servicio.login(usuario)
