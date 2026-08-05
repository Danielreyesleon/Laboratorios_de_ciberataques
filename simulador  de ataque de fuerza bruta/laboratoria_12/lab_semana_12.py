import time
import logging
"""
Simulador educativo de ataque de fuerza bruta.

Este script NO realiza ataques reales: su proposito es exclusivamente didactico.
Se utiliza como demostracion para entender la logica detras de un ataque de fuerza bruta,
sin causar dano, sin vulnerar sistemas y sin interactuar con servicios en produccion.

Usalo solo en entornos controlados y con autorizacion, como parte de practicas de ciberseguridad.
"""



logging.basicConfig(
    filename="intentos_exitosos.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"

)

def simulador_fuerzabruta(users, passwords, delay=0.3):
    print("<>------ simulador de ataque de fuerza bruta ------<>")   
    intento = 0
    exitosos = []
    
    for user in users:
        for password in passwords:
            intento += 1
            print(f"[Simulacion] intento {intento}: {user}: {password}")
            time.sleep(delay)
            
            if user == "admin" and password == "123456":
                mensaje = f"Credensiales correctos : ) -> {user}:{password}"
                print(mensaje)
                logging.info(mensaje)
                exitosos.append((user, password))
    print("\nDemo o simulador finalizado ")
    print(f"intentos del demo o simulador exitosos: {len(exitosos)}")

    return exitosos

if __name__ == "__main__":
    usuarios =["admin", "root", "test"]
    claves =["1234", "admin", "123456"]
    
    simulador_fuerzabruta(usuarios, claves)