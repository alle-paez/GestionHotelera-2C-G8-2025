from listas_codeadas import *

def llenar_reservas(matriz):
    nro_reserva = int(input("Ingrese el número de reserva (-1 para salir): "))
    while nro_reserva != -1:
        dni = int(input("Ingrese el DNI: "))
        cant_pax = int(input("Ingrese la cantidad de pasajeros: "))
        fecha_desde = input("Ingrese fecha inicio (AAAA-MM-DD): ")
        fecha_hasta = input("Ingrese fecha final (AAAA-MM-DD): ")
        total = int(input("Ingrese el total: "))

        matriz.append([nro_reserva, dni, cant_pax, fecha_desde, fecha_hasta, total])

        nro_reserva = int(input("Ingrese el número de reserva (-1 para salir): "))

def print_reservas(matriz):
    print("NroReserva|DNI       |Pax       |Desde     |Hasta     |Total     |")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            #print(espaciado(10, matriz[i][j], "i"), end="")
            print(f'{matriz[i][j]}'.center(10," "), end='')
        print()
    return matriz