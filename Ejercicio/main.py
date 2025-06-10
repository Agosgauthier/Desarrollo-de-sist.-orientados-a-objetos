from gestor_usuario import GestorUsuarios
from usuario_builder import UsuarioBuilder 

# Uso
gestor = GestorUsuarios.instancia or GestorUsuarios()

gestor.agregar(UsuarioBuilder().nombre("Agoss").correo("agoss@email.com").construir())
gestor.agregar(UsuarioBuilder().nombre("Carlos").correo("carlos@email.com").construir())

# Mostrar usuarios
for usuario in gestor.usuarios:
    print(usuario)
