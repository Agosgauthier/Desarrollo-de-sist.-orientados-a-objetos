from reloj import Reloj

reloj1 = Reloj(10, 30, 0)
reloj2 = Reloj(14, 45, 0)
reloj3 = Reloj(23, 59, 0)

print("Reloj 1:", reloj1.mostrar())
print("Reloj 2:", reloj2.mostrar())
print("Reloj 3:", reloj3.mostrar())

reloj1.sumar_minuto()
print("Reloj 1 después de sumar 1 minuto:", reloj1.mostrar())

reloj2.cambiar_hora(7, 0, 0)
print("Reloj 2 con nueva hora:", reloj2.mostrar())

if reloj1.es_diferente(reloj3):
    print("Reloj 1 y Reloj 3 tienen hora diferente")
else:
    print("Reloj 1 y Reloj 3 tienen la misma hora")