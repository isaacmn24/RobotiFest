from gpiozero import Robot
from time import sleep

izq_B_1A = 14
izq_B_1B = 15
izq_A_1A = 23
izq_A_1B = 24

der_B_1A = 2
der_B_1B = 3
der_A_1A = 4
der_A_1B = 17

motores_delante = (izq_B_1A, izq_B_1B), (der_B_1A, der_B_1B)
motores_atras = (izq_A_1A, izq_A_1B), (der_A_1A, der_A_1B)

ruedas_delanteras = Robot((izq_B_1A, izq_B_1B), (der_B_1A, der_B_1B))
ruedas_traseras = Robot((izq_A_1A, izq_A_1B), (der_A_1A, der_A_1B))

def mover_robot(direccion):
    if direccion == 'adelante':
        ruedas_delanteras.forward()
        ruedas_traseras.forward()
    elif direccion == 'atras':
        ruedas_delanteras.backward()
        ruedas_traseras.backward()
    elif direccion == 'detenerse':
        ruedas_delanteras.stop()
        ruedas_traseras.stop()
        
mover_robot("adelante")
sleep(60)
mover_robot("detenerse")
    
    