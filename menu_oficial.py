import random
import menu
from menu import *

def llenar_habitaciones(matriz):

    numero= int(input("Ingrese el número de habitación: "))
    while numero!=-1:
        
        precio=	int(input("Ingrese el precio: "))
        tipo=input("Ingrese el tipo de habitación: ")
        capacidad=int(input("Ingrese la capacidad de habitación: "))
        estado=input("Ingrese el estado de la habitación: ")

        matriz.append([numero, precio, tipo, capacidad, estado])

        numero= int(input("Ingrese el número de habitación: "))

def espaciado(largo, cadena, alineacion):
    cadena = str(cadena)
    largo_cadena = len(cadena)
    espacios_extra = largo - largo_cadena

    if espacios_extra < 0:
        espacios_extra = 0 

    if alineacion == "i":
        return cadena + " " * espacios_extra + "|"
    elif alineacion == "d":
        return " " * espacios_extra + cadena + "|"
    else:
        return cadena + "|"

def print_habitaciones(matriz):
    print("Número    |Precio    |Tipo      |Capacidad |Estado    |")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]} '.center(10," "), end="")
        print()
    return matriz

def crear_matriz(n,m):
    return [[0]*m for fil in range(n)]

def llenar_clientes(m):
    dni = int(input("Ingrese el Dni del cliente: (-1 para finalizar la carga:)"))
    while dni != -1: 
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        mail = input("Ingrese el e-mail del cliente: ")
        m.append([dni,nombre,apellido,telefono,mail])

        dni = int(input("Ingrese el Dni del cliente: (-1 para finalizar la carga:)"))        

def print_clientes(m):
    print("Dni	Nombre	Apellido	Teléfono	Mail")
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(espaciado(10,m[i][j], "i"), end = "")
        print()

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

def ubicar(matriz, item):
    flag=0
    i=0
    pos=-1
    while flag!=1:
        if matriz[i][0]==item:
            flag=1
            pos=i
        i+=1
        if i==len():
            flag=-1
    return pos

#menú
print("----Sistema de Gestión Hotelera----")
print("" "\n",
"1-Gestionar habitaciones", "\n", \
"2-Reservas", "\n", \
"Salir del programa con -1")
opcion=int(input("Ingrese numéricamente la opción deseada: "))

while opcion!=-1:
    if opcion==1:
        print("" \
        "1-Agregar habitación" , "\n", \
        "2-Modificar habitación" , "\n",\
        "3-Borrar habitación" , "\n",\
        "4-Ver habitaciones", "\n",\
        "Volver para atrás con -1")
        opcion_habitaciones=int(input("Ingrese numéricamente la opción deseada: "))

        while opcion_habitaciones!=-1:
            if opcion_habitaciones==1:
                llenar_habitaciones(habitaciones)
            elif opcion_habitaciones==2:
                print_habitaciones(habitaciones)
                item=input(int("Ingrese el número de habitación que quiera modificar: "))
            elif opcion_habitaciones==3:
                print_habitaciones(habitaciones)
                item=int(input("Ingrese el número de habitación que quiera eliminar: "))
                pos=ubicar(habitaciones, item)
                flag=1
                while flag==1:
                    if pos!=-1:
                        del(habitaciones[pos])
                        print(f'\nLa habitación {item} ha sido eliminada con éxito\n')
                        flag=int(input("Si quiere eliminar otra habitación ingrese 1, si no ingrese 0: "))
                        pos=-1
                    else:
                        item=int(input("La habitación ingresada no existe, intente de nuevo: "))

                    if flag==1:
                        item=int(input("Ingrese el número de habitación que quiera eliminar: "))
                        pos=ubicar(habitaciones, item)
            elif opcion_habitaciones==4:
                print_habitaciones(habitaciones)
            
            print(f'\
1-Agregar habitación\n\
2-Modificar habitación\n\
3-Borrar habitación\n\
4-Ver habitaciones\n\
Volver para atrás con -1')
            opcion_habitaciones=int(input("Ingrese numéricamente la opción deseada: "))

    elif opcion==2:
        print("" \
        "1-Agregar reserva" , "\n", \
        "2-Modificar reserva" , "\n",\
        "3-Cancelar reserva" , "\n",\
        "4-Ver reservas" , "\n",\
        "Volver para atrás con -1")
        opcion_reservas=int(input("Ingrese numéricamente la opción deseada: "))

        while opcion_reservas!=-1:

            if opcion_reservas==1:
                llenar_reservas(reservas)
            elif opcion_reservas==2:
                pass
            elif opcion_reservas==3:
                pass
            elif opcion_reservas==4:
                print_reservas(reservas)
            
            print("" \
            "1-Agregar reserva" , "\n", \
            "2-Modificar reserva" , "\n",\
            "3-Cancelar reserva" , "\n",\
            "4-Ver reservas" , "\n",\
            "Volver para atrás con -1")
            opcion_reservas=int(input("Ingrese numéricamente la opción deseada: "))

    print("" "\n",
    "1-Gestionar habitaciones", "\n", \
    "2-Reservas", "\n", \
    "Salir del programa con -1")
    opcion=int(input("Ingrese numéricamente la opción deseada: "))