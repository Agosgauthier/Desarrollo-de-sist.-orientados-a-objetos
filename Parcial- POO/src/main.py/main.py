from src.models.sala import Sala
from src.models.usuario import Usuario
from src.repositories.sala_repo import SalaRepository
from src.repositories.usuario_repo import UsuarioRepository
from src.repositories.reserva_repo import ReservaRepository
from src.services.reserva_service import ReservaService

if __name__ == "__main__":
    sala_repo = SalaRepository()
    usuario_repo = UsuarioRepository()
    reserva_repo = ReservaRepository()
    servicio = ReservaService(reserva_repo)

    sala = Sala(1, "Sala Azul", 10)
    usuario = Usuario(1, "Agoss", "agoss@email.com")

    sala_repo.agregar_sala(sala)
    usuario_repo.agregar_usuario(usuario)

    reserva = servicio.hacer_reserva(1, usuario, sala, "14:00", "15:00")
    print(reserva)
