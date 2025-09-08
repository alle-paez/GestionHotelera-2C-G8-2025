
def llenar_habitaciones(matriz):

    numero= int(input("Ingrese el número de habitación: "))
    while numero!=-1:
        
        precio=	int(input("Ingrese el precio: "))
        tipo=input("Ingrese el tipo de habitación: ")
        capacidad=int(input("Ingrese la capacidad de habitación: "))
        estado=input("Ingrese el estado de la habitación: ")

        matriz.append([numero, precio, tipo, capacidad, estado])

        numero= int(input("Ingrese el número de habitación: "))
        
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
            print(f'{m[i][j]}'.center(10," "), end = "")
        print()

