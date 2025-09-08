from datos.datos_hotel import *
from hotel.clientes import *
from hotel.habitaciones import *
from hotel.reservas import *
from hotel.login import *
from hotel.estadisticas import  mostrar_estadisticas
def ubicar(matriz, item): #INDEX
    flag=0
    i=0
    pos=-1
    while flag!=1:
        if matriz[i][0]==item:
            flag=1
            pos=i
        i+=1
        if i==len(matriz):
            flag=1
    return pos

mostrar_estadisticas()

#menú
print("----Sistema de Gestión Hotelera----")
print("" "\n",
"1-Gestionar habitaciones", "\n", \
"2-Reservas", "\n", \
"3-Ver Estadisticas", "\n", \
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
            if opcion_habitaciones==1:#AGREGAR HABITACIONES
                llenar_habitaciones(habitaciones)
                #AGREGAR CHECKEOS
            elif opcion_habitaciones==2: #MODIFICAR HABITACIONES
                #LO ESTÁ HACIENDO FACU
                print_habitaciones(habitaciones)
                item=input(int("Ingrese el número de habitación que quiera modificar: "))
            elif opcion_habitaciones==3: #ELIMINAR HABITACIONES
                #AGREGAR UN DESHACER¿
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
                        print("La habitación ingresada no existe, intente de nuevo")

                    if flag==1:
                        item=int(input("Ingrese el número de habitación que quiera eliminar: "))
                        pos=ubicar(habitaciones, item) #HACER UN CKECK ANTES PARA QUE NO SE CUELGUE SI SON MUCHOS ELEMENTOS¿
            elif opcion_habitaciones==4:#VER HABITACIONES
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

            if opcion_reservas==1: #AGREGAR RESERVA
                llenar_reservas(reservas)
            elif opcion_reservas==2: #MODIFICAR RESERVA
                pass
            elif opcion_reservas==3: # CANCELAR RESERVA
                pass
            elif opcion_reservas==4: #VER RESERVAS
                print_reservas(reservas)
            
            print(f'\
1-Agregar reserva\n\
2-Modificar reserva\n\
3-Cancelar reserva\n\
4-Ver reservas\n\
Volver para atrás con -1')
            opcion_reservas=int(input("Ingrese numéricamente la opción deseada: "))

    elif opcion==3:
        habitaciones.append("Puto")
        print_habitaciones(habitaciones)
        mostrar_habitacion()
    print(f'\n\
1-Gestionar habitaciones\n\
2-Reservas\n\
Salir del programa con -1')
    opcion=int(input("Ingrese numéricamente la opción deseada: "))

