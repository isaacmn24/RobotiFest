import servo
import motores
import camara
from time import sleep

# Cálculo del tiempo necesario para correr el rover a lazo abierto
diametro_rueda = 78                                 # mm
radio_rueda = diametro_rueda/2                      # mm
vel_angular = 30                                    # rpm
velocidad = vel_angular * radio_rueda / 1000 / 60   # m/s

def calcular_tiempo(distancia):                     # m
    tiempo_requerido = distancia/velocidad          # s
    return tiempo_requerido

# Cierro la garra
servo.cerrar_garra()

# Avanzo distancia para bajar rampa y colocar bandera
for motor in range(4):
    motores.Avance(motor)
distancia_bandera = 3                               # m
tiempo_bandera = calcular_tiempo(distancia_bandera) # s
sleep(tiempo_bandera)

# Detengo los motores y doy media vuelta
for motor in range(4):
    motores.Paro(motor)
motores.Giro180()

# Retrocedo para tomar foto
for motor in range(4):
    motores.Retroceso(motor)
distancia_foto = 1                                  # m
tiempo_foto = calcular_tiempo(distancia_foto)       # s
sleep(tiempo_foto)

# Tomo foto de bandera y la envío por correo
foto = camara.tomar_foto()
camara.enviar_correo(foto)

