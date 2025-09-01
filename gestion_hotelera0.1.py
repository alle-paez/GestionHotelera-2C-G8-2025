import random
# Clientes titulares
clientes = [
    [30555999, "Juan", "Pérez", "1123456789", "juan.perez@email.com"],
    [28444888, "María", "Gómez", "1167894321", "maria.gomez@email.com"],
    [33222111, "Lucas", "Martínez", "1134567890", "lucas.martinez@email.com"],
    [29888777, "Sofía", "López", "1145678901", "sofia.lopez@email.com"],
    [31222333, "Martín", "Díaz", "1178901234", "martin.diaz@email.com"]
]

# Habitaciones
habitaciones = [
    [101, 15000, "Doble", 2, "Disponible"],
    [102, 20000, "Triple", 3, "Ocupada"],
    [103, 18000, "Doble", 2, "Mantenimiento"],
    [104, 25000, "Suite", 4, "Disponible"],
    [105, 12000, "Single", 1, "Disponible"]
]

# Reservas
reservas = [
    [1, 30555999, 2, "2025-08-15", "2025-08-20", 0, 75000],
    [2, 28444888, 3, "2025-08-18", "2025-08-25", 10, 126000],
    [3, 33222111, 2, "2025-09-01", "2025-09-05", 0, 72000],
    [4, 29888777, 4, "2025-08-10", "2025-08-15", 15, 106250],
    [5, 31222333, 1, "2025-08-22", "2025-08-24", 5, 22800]
]
tipos   = ["Single", "Doble", "Triple", "Suite"]
estados = ["Disponible", "Ocupada", "Mantenimiento"]

def buscar_indice_en_col(matriz, col, valor):
    i = 0
    while i < len(matriz) and matriz[i][col] != valor:
        i = i + 1
    if i == len(matriz):
        return -1
    return i

def llenar_habitaciones(matriz):
    numero = int(input("Número de habitación (-1 para salir): "))

    while numero != -1:
        while numero < 1 and numero != -1:
            print("El número debe ser > 0 (o -1 para salir).")
            numero = int(input("Número de habitación (-1 para salir): "))

        if numero != -1:
            idx = buscar_indice_en_col(matriz, 0, numero)
            while idx != -1 and numero != -1:
                print("Esta habitación ya existe.")
                numero = int(input("Número de habitación (-1 para salir): "))
                while numero < 1 and numero != -1:
                    print("El número debe ser > 0 (o -1 para salir).")
                    numero = int(input("Número de habitación (-1 para salir): "))
                if numero != -1:
                    idx = buscar_indice_en_col(matriz, 0, numero)

            if numero != -1 and idx == -1:
                precio = int(input("Precio (entero > 0): "))
                while precio < 1:
                    precio = int(input("Precio inválido. Precio (entero > 0): "))

                tipo = int(input("Tipo: 1/Single  2/Doble  3/Triple  4/Suite: "))
                while tipo < 1 or tipo > 4:
                    tipo = int(input("Opción inválida. Tipo (1-4): "))
                tipo_txt = tipos[tipo - 1]

                capacidad = int(input("Capacidad (> 0): "))
                while capacidad < 1:
                    capacidad = int(input("Capacidad inválida. Capacidad (> 0): "))

                estado = int(input("Estado: 1/Disponible  2/Ocupada  3/Mantenimiento: "))
                while estado < 1 or estado > 3:
                    estado = int(input("Opción inválida. Estado (1-3): "))
                estado_txt = estados[estado - 1]

                matriz.append([numero, precio, tipo_txt, capacidad, estado_txt])
                print("Habitación agregada.")

                numero = int(input("Número de habitación (-1 para salir): "))

def modificar_habitacion(matriz):
    numero = int(input("Número de habitación a modificar (-1 para volver): "))
    while numero != -1:
        idx = buscar_indice_en_col(matriz, 0, numero)
        while idx == -1 and numero != -1:
            print("No existe esa habitación.")
            numero = int(input("Número de habitación a modificar (-1 para volver): "))
            if numero != -1:
                idx = buscar_indice_en_col(matriz, 0, numero)

        if numero != -1:
            fila = matriz[idx]  # [nro, precio, tipo_txt, capacidad, estado_txt]
            print("\nActual →",
                  "Nro:", fila[0],
                  "Precio:", fila[1],
                  "Tipo:", fila[2],
                  "Capacidad:", fila[3],
                  "Estado:", fila[4])

            op = int(input("\n¿Qué modificar?  1-Precio  2-Tipo  3-Capacidad  4-Estado  5-Todos  (-1 volver)\nOpción: "))
            while op != -1:
                if op == 1:
                    nuevo = int(input("Nuevo precio (> 0): "))
                    while nuevo < 1:
                        nuevo = int(input("Precio inválido. Nuevo precio (> 0): "))
                    matriz[idx][1] = nuevo
                    print("Precio actualizado.")

                elif op == 2:
                    print("Tipos: 1/Single  2/Doble  3/Triple  4/Suite")
                    t = int(input("Elegí tipo (1-4): "))
                    while t < 1 or t > 4:
                        t = int(input("Opción inválida. Elegí tipo (1-4): "))
                    matriz[idx][2] = tipos[t-1]
                    print("Tipo actualizado.")

                elif op == 3:
                    cap = int(input("Nueva capacidad (> 0): "))
                    while cap < 1:
                        cap = int(input("Capacidad inválida (> 0): "))
                    matriz[idx][3] = cap
                    print("Capacidad actualizada.")

                elif op == 4:
                    print("Estados: 1/Disponible  2/Ocupada  3/Mantenimiento")
                    e = int(input("Elegí estado (1-3): "))
                    while e < 1 or e > 3:
                        e = int(input("Opción inválida. Elegí estado (1-3): "))
                    matriz[idx][4] = estados[e-1]
                    print("Estado actualizado.")

                elif op == 5:
                    nuevo = int(input("Nuevo precio (> 0): "))
                    while nuevo < 1:
                        nuevo = int(input("Precio inválido. Nuevo precio (> 0): "))
                    print("Tipos: 1/Single  2/Doble  3/Triple  4/Suite")
                    t = int(input("Elegí tipo (1-4): "))
                    while t < 1 or t > 4:
                        t = int(input("Opción inválida. Elegí tipo (1-4): "))
                    cap = int(input("Nueva capacidad (> 0): "))
                    while cap < 1:
                        cap = int(input("Capacidad inválida (> 0): "))
                    print("Estados: 1/Disponible  2/Ocupada  3/Mantenimiento")
                    e = int(input("Elegí estado (1-3): "))
                    while e < 1 or e > 3:
                        e = int(input("Opción inválida. Elegí estado (1-3): "))

                    matriz[idx][1] = nuevo
                    matriz[idx][2] = tipos[t-1]
                    matriz[idx][3] = cap
                    matriz[idx][4] = estados[e-1]
                    print("Todos los campos actualizados.")

                else:
                    print("Opción inválida.")

                op = int(input("\n1-Precio  2-Tipo  3-Capacidad  4-Estado  5-Todos  (-1 volver)\nOpción: "))

            numero = int(input("\nNúmero de otra habitación a modificar (-1 para volver): "))



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
            print(str(matriz[i][j]).center(10), end="")
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
            print(f'{matriz[i][j]}'.center(10,0), end='')
        print()
    return matriz



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
                modificar_habitacion(habitaciones)
            elif opcion_habitaciones==3:
                pass
            elif opcion_habitaciones==4:
                print_habitaciones(habitaciones)
            else:
                print("Opcion invalida")
            
            print("" \
            "1-Agregar habitación" , "\n", \
            "2-Modificar habitación" , "\n",\
            "3-Borrar habitación" , "\n",\
            "4-Ver habitaciones", "\n",\
            "Volver para atrás con -1")
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

            llenar_reservas(reservas)
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



