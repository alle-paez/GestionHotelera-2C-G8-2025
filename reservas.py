from listas_codeadas import *
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


def verificar_formato_fecha(fecha):
    formato = r"^\d{4}-\d{2}-\d{2}$"
    if re.match(formato, fecha):
        return True
    else:
        return False
        
def separar_en_lista(fecha):
    matriz_fecha = fecha.split('-')
    anio = int(matriz_fecha[0])
    mes = int(matriz_fecha[1])
    dia = int(matriz_fecha[2])
    return [anio, mes, dia]

def bisiesto(anio):
    return((anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0))

def verificar_ingresos_fecha(fecha):
    if fecha[1] < 1 or fecha[1] > 12:
        return False


    if fecha[2] < 1 or fecha[2] > dias_en_mes(fecha[0], fecha[1]):
        return False
    
    return True
    
def verificar_egreso(check_in, check_out):
    if tuple(check_out) <= tuple(check_in):
        return False 
    else: 
        return True

def pedir_fecha(mensaje):
    valido = False
    while not valido:
        fecha_str = input(mensaje)
        if verificar_formato_fecha(fecha_str):
            fecha = separar_en_lista(fecha_str)
            if verificar_ingresos_fecha(fecha):
                valido = True
            else:
                print("La fecha no existe, vuelva a intentar.")
        else:
            print("Formato incorrecto, use AAAA-MM-DD.")
    return fecha  #Sale [año, mes, dia]

def dias_en_mes(anio, mes):
    dias_mes = [31, 29 if bisiesto(anio) else 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]
    return dias_mes[mes - 1]


def contar_dias(fecha):
    anio, mes, dia = fecha
    for a in range(1, anio):
        dias += 366 if bisiesto(a) else 365
        for m in range(1, mes):
            dias += dias_en_mes(anio, m)
        
        dias += dia
        return dias

def diferencia_dias_entre(check_in, check_out):
    return contar_dias(check_out) - contar_dias(check_in)

def llenar_reservas(matriz):
    nro_dni= int(input("Ingrese el número de dni del cliente: (-1 para salir): "))
    while nro_dni != -1:

        cant_pax = int(input("Ingrese la cantidad de pasajeros: "))
#CHECK-IN Y CHECK-OUT ------------------------------------------------------------------------------------------------------
        check_in = pedir_fecha("Ingrese fecha inicio (AAAA-MM-DD): ")
        check_out = pedir_fecha("Ingrese fecha final (AAAA-MM-DD): ")
        while not verificar_egreso(check_in, check_out):
            print("El egreso debe ser posterior al ingreso.")
            check_out = pedir_fecha("Reingrese fecha fin (AAAA-MM-DD): ")

        dias = diferencia_dias_entre(check_in, check_out)
        if dias > 31:
            continuar = int(input("Cantidad de días mayor a 31, desea continuar? 1 - Si | 2 - No "))
            while continuar != 1 or continuar != 2:
                print("Se debe ingresar 1 o 2.")
                continuar = int(input("Cantidad de días mayor a 31, desea continuar? 1 - Si | 2 - No "))
            if continuar == 1:
                pass
            if continuar == 2:
                pass 

        total = int(input("Ingrese el total: "))
        nro_reserva = len(matriz) + 1


def print_reservas(matriz):
    print("NroReserva|DNI       |Pax       |Desde     |Hasta     |Total     |")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            #print(espaciado(10, matriz[i][j], "i"), end="")
            print(f'{matriz[i][j]}'.center(10," "), end='')
        print()
    return matriz


