from datos.datos_hotel import habitaciones

def disponibilidad_habitacion():
    for habitacion in habitaciones:
        if habitacion[4]== "Disponible":
            print(habitacion)



def mostrar_estadisticas():
    disponibilidad_habitacion()
    