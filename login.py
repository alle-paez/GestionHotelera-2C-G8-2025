usuarios_db = [
    [1, "cliente1", "pass123", "cliente", 1],
    [2, "admin1", "admin456", "empleado", 1],
    [3, "cliente2", "clave789", "cliente", 0],
    ]

def autenticar_usuario(nombre, contrasenia):
    """
    Función que busca un usuario por nombre y contraseña.
    Retorna un diccionario con los datos del usuario si es válido y está activo.
    Retorna None si falla la autenticación.
    """
    for usuario in usuarios_db:
        id_user, nom_user, pass_user, rol_user, activo_user = usuario
        if nom_user == nombre and pass_user == contrasenia and activo_user == 1:
            return {
                "id": id_user,
                "nombre": nom_user,
                "rol": rol_user
            }
    return None

# Función ejemplo para dar de baja un usuario (baja lógica)
def dar_de_baja_usuario(id_usuario):
    for usuario in usuarios_db:
        if usuario[0] == id_usuario:
            usuario[4] = 0  # Cambia 'activo' a 0
            print(f"Usuario con ID {id_usuario} dado de baja lógicamente.")
            return True
    print(f"Usuario con ID {id_usuario} no encontrado.")
    return False

# menu_cliente.py
def mostrar_menu_cliente():
    print("\n=== Menú Cliente ===")
    print("1. Ver mis reservas")
    print("2. Realizar una reserva")
    print("3. Salir")

def ejecutar_menu_cliente():
    while True:
        mostrar_menu_cliente()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("Mostrando sus reservas...")
            # Aquí iría la lógica para mostrar reservas
        elif opcion == "2":
            print("Iniciando proceso de reserva...")
            # Aquí iría la lógica para hacer una reserva
        elif opcion == "3":
            print("Cerrando sesión de cliente.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# menu_empleado.py

# from usuarios import dar_de_baja_usuario

def mostrar_menu_empleado():
    print("\n=== Menú Empleado (Administrador) ===")
    print("1. Gestionar habitaciones")
    print("2. Ver todas las reservas")
    print("3. Dar de baja un usuario (baja lógica)")
    print("4. Salir")

def ejecutar_menu_empleado():
    while True:
        mostrar_menu_empleado()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("Gestionando habitaciones...")
            # Lógica para gestionar habitaciones
        elif opcion == "2":
            print("Mostrando todas las reservas...")
            # Lógica para ver todas las reservas
        elif opcion == "3":
            try:
                id_baja = int(input("Ingrese el ID del usuario a dar de baja: "))
                dar_de_baja_usuario(id_baja)
            except ValueError:
                print("ID inválido. Debe ser un número.")
        elif opcion == "4":
            print("Cerrando sesión de empleado.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# main.py

#from usuarios import autenticar_usuario
#from menu_cliente import ejecutar_menu_cliente
#from menu_empleado import ejecutar_menu_empleado

def main():
    print("=== Bienvenido al Sistema del Hotel ===")
    
    nombre = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    
    usuario = autenticar_usuario(nombre, contrasena)
    
    if usuario:
        print(f"Login exitoso. Bienvenido, {usuario['nombre']} ({usuario['rol']}).")
        
        # Redirigir al menú según el rol
        if usuario['rol'] == 'cliente':
            ejecutar_menu_cliente()
        elif usuario['rol'] == 'empleado':
            ejecutar_menu_empleado()
    else:
        print("Error: Nombre de usuario o contraseña incorrectos, o usuario inactivo.")

if __name__ == "__main__":
    main()

# utils.py

#from usuarios import usuarios_db

def obtener_usuarios_activos():
    """
    Retorna una lista de usuarios que están activos (baja lógica = 1).
    Usa filter y lambda para filtrar la matriz.
    """
    # Filtramos las filas donde el campo 'activo' (índice 4) es 1
    activos = list(filter(lambda usuario: usuario[4] == 1, usuarios_db))
    return activos

# Ejemplo de uso (podrías llamarlo desde menu_empleado.py)
if __name__ == "__main__":
    activos = obtener_usuarios_activos()
    for usr in activos:
        print(f"Usuario activo: {usr[1]} ({usr[3]})")