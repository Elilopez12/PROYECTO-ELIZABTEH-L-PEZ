from funciones import *


class Cliente:
    def __init__(self, nombre, tipo, identificacion, correo, direccion, telefono):
        self.nombre = nombre
        self.tipo = tipo
        self.identificacion = identificacion
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono


class Gestiondeclientes:
    def __init__(self):
        self.clientes = []

    def registrar_cliente(self):
        nombre = input("Ingrese el nombre y apellido o razón social del cliente: ")
        validar(nombre, "Texto", None, None)
        tipo = input("Ingrese el tipo de cliente (Natural o Jurídico): ")
        validar(tipo, "TextCon", ["Jurídico", "Natural"],None)
        identificacion = input("Ingrese la cédula o RIF del cliente: ")
        validar(identificacion, "C.I", None, None)
        correo = input("Ingrese el correo electrónico del cliente: ")
        direccion = input("Ingrese la dirección de envío del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        validar(telefono,"C.I", None, None)
        nuevo_cliente = Cliente(nombre, tipo, identificacion, correo, direccion, telefono)
        self.clientes.append(nuevo_cliente)
        print("Cliente registrado con éxito.")
    def show_cliente():
        return f"nuevo_cliente"
        


    def modificar_cliente(self):
        identificacion = input("Ingrese la cédula o RIF del cliente que desea modificar: ")
        encontrado = False

        for cliente in self.clientes:
            if cliente.identificacion == identificacion:
                nuevo_nombre = input(f"Ingrese el nuevo nombre y apellido o razón social para el cliente {cliente.nombre}: ")
                nuevo_tipo = input(f"Ingrese el nuevo tipo de cliente para el cliente {cliente.nombre}: ")
                nuevo_correo = input(f"Ingrese el nuevo correo electrónico para el cliente {cliente.nombre}: ")
                nueva_direccion = input(f"Ingrese la nueva dirección de envío para el cliente {cliente.nombre}: ")
                nuevo_telefono = input(f"Ingrese el nuevo teléfono para el cliente {cliente.nombre}: ")
                cliente.nombre = nuevo_nombre
                cliente.tipo = nuevo_tipo
                cliente.correo = nuevo_correo
                cliente.direccion = nueva_direccion
                cliente.telefono = nuevo_telefono

                print("Cliente modificado con éxito.")
                encontrado = True
                break

        if not encontrado:
            print("No se encontró un cliente con la cédula o RIF ingresado.")


    def eliminar_cliente(self):
        identificacion = input("Ingrese la cédula o RIF del cliente que desea eliminar: ")
        encontrado = False

        for cliente in self.clientes:
            if cliente.identificacion == identificacion:
                self.clientes.remove(cliente)
                print("Cliente eliminado con éxito.")
                encontrado = True
                break

        if not encontrado:
            print("No se encontró un cliente con la cédula o RIF ingresado.")


    def buscar_cliente_por_identificacion(self):
        identificacion = input("Ingrese la cédula o RIF del cliente que desea buscar: ")

        for cliente in self.clientes:
            if cliente.identificacion == identificacion:
                print("Información del cliente encontrado:")
                print(f"Nombre: {cliente.nombre}")
                print(f"Tipo: {cliente.tipo}")
                print(f"Correo electrónico: {cliente.correo}")
                print(f"Dirección de envío: {cliente.direccion}")
                print(f"Teléfono: {cliente.telefono}")
                return

        print("No se encontró un cliente con la cédula o RIF ingresado.")


    def buscar_cliente_por_correo(self):
        correo = input("Ingrese el correo electrónico del cliente que desea buscar: ")

        for cliente in self.clientes:
            if cliente.correo == correo:
                print("Información del cliente encontrado:")
                print(f"Nombre: {cliente.nombre}")
                print(f"Tipo: {cliente.tipo}")
                print(f"Cédula o RIF: {cliente.identificacion}")
                print(f"Dirección de envío: {cliente.direccion}")
                print(f"Teléfono: {cliente.telefono}")
                return

        print("No se encontró un cliente con el correo electrónico ingresado.")


tienda = Gestiondeclientes()

def menuclientes():
    while True:
        print("          -------- [ Menú ] --------          \n")
        print("     1. Registrar nuevo cliente")
        print("     2. Modificar información de cliente")
        print("     3. Eliminar cliente")
        print("     4. Buscar cliente por cédula o RIF")
        print("     5. Buscar cliente por correo electrónico")
        print("     6. Salir")
        opcion = input("     Ingrese el número de opción deseada: ")

        if opcion == "1":
            tienda.registrar_cliente()
        elif opcion == "2":
            tienda.modificar_cliente()
        elif opcion == "3":
            tienda.eliminar_cliente()
        elif opcion == "4":
            tienda.buscar_cliente_por_identificacion()
        elif opcion == "5":
            tienda.buscar_cliente_por_correo()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    print("Gracias por utilizar el sistema de gestión de clientes.")
    
menuclientes()
    


    
