class ReservaRepository:
      def __init__(self):
        self.reservas = []

      def agregar_reserva(self, sala, usuario, inicio, fin):
        reserva = {
            "sala": sala.nombre,
            "usuario": usuario.correo,
            "inicio": inicio,
            "fin": fin
        }
        self.reservas.append(reserva)
        return reserva
