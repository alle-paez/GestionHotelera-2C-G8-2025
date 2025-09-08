from listas_codeadas import habitaciones
from auxiliar_habitaciones import *

def print_habitaciones(matriz):
    print("Número    |Precio    |Tipo      |Capacidad |Estado    |")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]} '.center(10, " "), end="")
        print()
    return matriz

def llenar_habitaciones(matriz):
    numero = leer_numero("Número de habitación (-1 para salir): ", permitir_menos1=True)

    while numero != -1:
        idx = ubicar(matriz, numero)
        while idx != -1 and numero != -1:
            print("Esta habitación ya existe.")
            numero = leer_numero("Número de habitación (-1 para salir): ", permitir_menos1=True)
            if(numero != -1):
                idx = ubicar(matriz, numero)

        if numero != -1 and idx == -1:
            precio = leer_numero("Precio (entero > 0): ")

            tipo_txt = leer_tipo()
            capacidad = leer_numero("Capacidad (> 0): ")
            estado_txt = leer_estado()

            matriz.append([numero, precio, tipo_txt, capacidad, estado_txt])
            print("Habitación agregada.")

            numero = leer_numero("Número de habitación (-1 para salir): ", permitir_menos1=True)

def modificar_habitacion(matriz):
    numero = leer_numero("Número de habitación a modificar (-1 para volver): ", permitir_menos1=True)

    while numero != -1:
        idx = ubicar(matriz, numero)
        while idx == -1 and numero != -1:
            print("No existe esa habitación.")
            numero = leer_numero("Número de habitación a modificar (-1 para volver): ", permitir_menos1=True)
            if numero != -1:
                idx = ubicar(matriz, numero)

        if numero != -1:
            fila = matriz[idx]  # [nro, precio, tipo, capacidad, estado]
            print("\nActual →",
                  "Nro:", fila[0],
                  "Precio:", fila[1],
                  "Tipo:", fila[2],
                  "Capacidad:", fila[3],
                  "Estado:", fila[4])

            op_txt = input("\n¿Qué modificar?  1-Precio  2-Tipo  3-Capacidad  4-Estado  5-Todos  (-1 volver)\nOpción: ").strip()
            while not (op_txt.lstrip("-").isdigit() and int(op_txt) in {1,2,3,4,5,-1}):
                print("Opción inválida.")
                op_txt = input("\n1-Precio  2-Tipo  3-Capacidad  4-Estado  5-Todos  (-1 volver)\nOpción: ").strip()
            op = int(op_txt)

            while op != -1:
                if op == 1:
                    nuevo = leer_numero("Nuevo precio (> 0): ")
                    matriz[idx][1] = nuevo
                    print("Precio actualizado.")

                elif op == 2:
                    matriz[idx][2] = leer_tipo()
                    print("Tipo actualizado.")

                elif op == 3:
                    cap = leer_numero("Nueva capacidad (> 0): ")
                    matriz[idx][3] = cap
                    print("Capacidad actualizada.")

                elif op == 4:
                    matriz[idx][4] = leer_estado()
                    print("Estado actualizado.")

                elif op == 5:
                    nuevo = leer_numero("Nuevo precio (> 0): ")
                    t_txt = leer_tipo()
                    cap = leer_numero("Nueva capacidad (> 0): ")
                    e_txt = leer_estado()

                    matriz[idx][1] = nuevo
                    matriz[idx][2] = t_txt
                    matriz[idx][3] = cap
                    matriz[idx][4] = e_txt
                    print("Todos los campos actualizados.")

                op_txt = input("\n1-Precio  2-Tipo  3-Capacidad  4-Estado  5-Todos  (-1 volver)\nOpción: ").strip()
                while not (op_txt.lstrip("-").isdigit() and int(op_txt) in {1,2,3,4,5,-1}):
                    print("Opción inválida.")
                    op_txt = input("\n1-Precio  2-Tipo  3-Capacidad  4-Estado  5-Todos  (-1 volver)\nOpción: ").strip()
                op = int(op_txt)

            numero = leer_numero("\nNúmero de otra habitación a modificar (-1 para volver): ", permitir_menos1=True)

def eliminar_habitacion(matriz):
    if len(matriz) == 0:
        print("No hay habitaciones cargadas para eliminar.")
        return

    print_habitaciones(matriz)
    item = leer_numero("Ingrese el número de habitación que quiera eliminar (-1 para volver): ", permitir_menos1=True)
    pos = ubicar(matriz, item)
    flag = 1
    while flag == 1 and item != -1:
        if pos != -1:
            del(matriz[pos])
            print(f'\nLa habitación {item} ha sido eliminada con éxito\n')
            flag = leer_numero("Si quiere eliminar otra habitación ingrese 1, si no ingrese 0: ")
            pos = -1
        else:
            print("La habitación ingresada no existe, intente de nuevo")

        if flag == 1:
            item = leer_numero("Ingrese el número de habitación que quiera eliminar (-1 para volver): ", permitir_menos1=True)
            pos = ubicar(matriz, item)


# --- menú principal ---
def menu_habitaciones():

    opcion = 0
    while opcion != -1:
        print("\n=== MENÚ HABITACIONES ===")
        print("1 - Agregar habitaciones")
        print("2 - Modificar una habitación")
        print("3 - Ver habitaciones")
        print("-1 - Salir")

        entrada = input("Opción: ")
        if entrada.lstrip("-").isdigit():
            opcion = int(entrada)
        else:
            print("Elegí un número válido.")
            opcion = 0

        if opcion == 1:
            llenar_habitaciones(habitaciones)
        elif opcion == 2:
            if len(habitaciones) == 0:
                print("No hay habitaciones cargadas para modificar.")
            else:
                modificar_habitacion(habitaciones)
        elif opcion == 3:
            eliminar_habitacion(habitaciones)
        elif opcion == 4:
            print_habitaciones(habitaciones)

        elif opcion == -1:
            print("Saliendo...")
        else:
            if opcion != 0:
                print("Opción inválida.")


if __name__ == "__main__":
    menu_habitaciones()

