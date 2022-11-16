from Desktop_Alert import Alert

def_Alert=Alert()

Amessage=input("Cual es el texto de tu recordatorio\n")
time=input("Tiempo de la alerta expresado en minuntos\n")
time =int(time)*60
timeout=input("Cuantas veces se ejecutará\n")
timeout=int(timeout)

Nueva_Alerta = def_Alert.Alerta(Amessage,time,timeout)
