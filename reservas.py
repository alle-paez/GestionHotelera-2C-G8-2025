from listas_codeadas import *
from datetime import datetime
import re

"""Lista para hacer: 

reservas = [
    [1, 30555999, 2, [2025,08,15], [2025,08,20], 101, 75000],
    [2, 28444888, 3, [2025,08,18], [2025,08,25], 102, 126000],
    [3, 33222111, 2, [2025,09,01], [2025,09,05], 103, 72000],
    [4, 29888777, 4, [2025,08,10], [2025,08,15], 104, 106250],
    [5, 31222333, 1, [2025,08,22], [2025,08,24], 105, 22800]
    ]
    - Validar si existe el cliente, si no, crearlo.
    - Validar si la habitacion solicitada no esta ocupada en la fecha seleccionada.
    - falta el precio por noche, tiene que estar cargado en la lista habitaciones.
     """

def definir_fechas(fecha_ingresada):
     fecha = datetime.strptime(fecha_ingresada, "%Y-%m-%d").date()
     return fecha

def verificar_formato_fecha(fecha):
    formato = r"^\d{4}-\d{2}-\d{2}$"
    if re.match(formato, fecha):
        return 0
    else:
        return 1
        
        
def llenar_reservas(matriz):
    nro_dni= int(input("Ingrese el número de dni del cliente: (-1 para salir): "))
    while nro_dni != -1:
        cant_pax = int(input("Ingrese la cantidad de pasajeros: "))
        checkin_str = input("Ingrese fecha inicio (AAAA-MM-DD): ")
    
        checkout_str = input("Ingrese fecha final (AAAA-MM-DD): ")
        total = int(input("Ingrese el total: "))

        nro_reserva = matriz(len(matriz)) + 1
        check_in = definir_fechas(checkin_str)
        check_out = definir_fechas(checkout_str)

        ver = verificar_dias(check_in, check_out)
        if ver == 1:
            print("La fecha de terminación no puede ser anterior a la de inicio.")
        elif ver == 2:
            ver_fecha_larga = int(input("Se ingreso una fecha muy larga, desea continuar? ( 1 -  Si |  2 - No )"))
            while ver_fecha_larga != 1 or ver_fecha_larga != 2:
                ver_fecha_larga = int(input("Se ingreso una fecha muy larga, desea continuar? ( 1 -  Si |  2 - No )"))
                
                if ver_fecha_larga == 1:
                    #matriz.append([nro_reserva])
                    pass
                if ver_fecha_larga == 2:
                    nro_dni= int(input("Ingrese el número de dni del cliente: (-1 para salir): "))
        elif ver == 0:
            matriz.append([nro_reserva, nro_dni, cant_pax, check_in, check_out, total])
            nro_dni= int(input("Ingrese el número de dni del cliente: (-1 para salir): "))

def verificar_dias(checkin,checkout):
    dias = checkout - checkin
    if dias < 0:
        return 1
    elif dias > 60:
        return 2
    else:
        return 0
def print_reservas(matriz):
    print("NroReserva|DNI       |Pax       |Desde     |Hasta     |Total     |")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            #print(espaciado(10, matriz[i][j], "i"), end="")
            print(f'{matriz[i][j]}'.center(10," "), end='')
        print()
    return matriz