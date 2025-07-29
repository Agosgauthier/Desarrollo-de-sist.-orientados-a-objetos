from src.models.sala import Sala

class FactorySala:
    def crear_sala(self, id, nombre, capacidad):
        return Sala(id, nombre, capacidad)