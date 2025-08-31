reservas = [
    [1, 30555999, 2, "2025-08-15", "2025-08-20", 0, 75000],
    [2, 28444888, 3, "2025-08-18", "2025-08-25", 10, 126000],
    [3, 33222111, 2, "2025-09-01", "2025-09-05", 0, 72000],
    [4, 29888777, 4, "2025-08-10", "2025-08-15", 15, 106250],
    [5, 31222333, 1, "2025-08-22", "2025-08-24", 5, 22800]
]

habitaciones = [
    [101, 15000, "Doble", 2, "Disponible"],
    [102, 20000, "Triple", 3, "Ocupada"],
    [103, 18000, "Doble", 2, "Mantenimiento"],
    [104, 25000, "Suite", 4, "Disponible"],
    [105, 12000, "Single", 1, "Disponible"]
]

clientes = [
    [30555999, "Juan", "Pérez", "1123456789", "juan.perez@email.com"],
    [28444888, "María", "Gómez", "1167894321", "maria.gomez@email.com"],
    [33222111, "Lucas", "Martínez", "1134567890", "lucas.martinez@email.com"],
    [29888777, "Sofía", "López", "1145678901", "sofia.lopez@email.com"],
    [31222333, "Martín", "Díaz", "1178901234", "martin.diaz@email.com"]
]

def alta_clientes(clientes):
    dni_cliente = int(input("Ingrese el dni del cliente: (-1 para salir) "))
    while dni_cliente != -1:
        if dni_cliente in clientes:
            print("Se ingreso un cliente ya existente. Por favor, ingrese otro.")
            dni_cliente = int(input("Ingrese el dni del cliente: (-1 para salir) "))
        else: 
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            apellido_cliente = input("Ingrese el apellido del cliente: ")
            telefono_cliente = int(input("Ingrese el telefono del cliente: "))
            mail_cliente = input("Ingrese el mail del cliente: ")

            clientes.append([dni_cliente, nombre_cliente, apellido_cliente, telefono_cliente, mail_cliente])
            dni_cliente = int(input("Ingrese el dni del cliente: (-1 para salir) "))


