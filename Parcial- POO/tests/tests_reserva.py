import unittest
from src.models.reserva import Reserva

class TestReserva(unittest.TestCase):
    def test_creacion_reserva(self):
        reserva = Reserva(1, "Usuario1", "Sala1", "10:00", "11:00")
        self.assertEqual(reserva.sala, "Sala1")
