from datetime import datetime

class ReservaServicio:
    def __init__(self, reserva_repo):
        self.reserva_repo = reserva_repo

    def hacer_reserva(self, id, usuario, sala, hora_inicio, hora_fin):
        if self.reserva_repo.hay_conflicto(sala, hora_inicio, hora_fin):
             raise Exception("La sala ya está reservada en ese horario.")
        return self.reserva_repo.agregar_reserva(sala, usuario, hora_inicio, hora_fin)
    