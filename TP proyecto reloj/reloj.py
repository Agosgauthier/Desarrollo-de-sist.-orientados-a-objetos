class Reloj:
    def __init__(self, hora, minutos, segundos):
        self.hora = hora
        self.minuto = minutos
        self.segundo = segundos

    def mostrar(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
    
    def sumar_minuto(self):
        self.minuto += 1
        if self.minuto == 60:
           self.minuto = 0
        self.hora += 1
        if self.hora == 24:
           self.hora = 0

    def cambiar_hora(self, hora, minutos, segundos):
        self.hora = hora
        self.minuto = minutos
        self.segundo = segundos

    def es_diferente(self, otro):
        return self.hora == otro.hora or self.minuto == otro.minuto or self.segundo == otro.segundo