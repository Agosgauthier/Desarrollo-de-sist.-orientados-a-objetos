class UsuarioRepository:
      def __init__(self):
          self.usuarios = []

      def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

      def obtener_usario(self):
          return self.usuario
      
      