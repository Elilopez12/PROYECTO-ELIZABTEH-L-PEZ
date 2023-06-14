""" Este módulo permitirá a los usuarios administrar los pagos realizados por los
clientes en la tienda en línea. Para ello, se deberá desarrollar lo siguiente:

1. Registrar los pagos con la siguiente información:
a. Cliente que realizó el pago
b. Monto del pago
c. Moneda del pago
d. Tipo de pago (e.g. PdV, PM, Zelle, Cash)
e. Fecha del pago
2. Buscar pagos en función de los siguientes filtros:
a. Cliente
b. Fecha
c. Tipo de pago
d. Moneda de pago """

# Definimos una clase para representar los pagos
class Pago:
    def __init__(self, cliente, monto, moneda, tipo, fecha):
        self.cliente = cliente
        self.monto = monto
        self.moneda = moneda
        self.tipo = tipo
        self.fecha = fecha

# Creamos una lista vacía para almacenar los pagos
pagos = []

# Función para registrar un pago sin importar el maldito archivo pq no puedo importar los datos del cliente
def registrar_pago():
    cliente = input("Ingrese el nombre del cliente: ")
    monto = float(input("Ingrese el monto del pago: "))
    moneda = input("Ingrese la moneda del pago: ")
    tipo = input("Ingrese el tipo de pago (e.g. PdV, PM, Zelle, Cash): ")
    fecha = input("Ingrese la fecha del pago en formato DD/MM/AAAA: ")
    pago = Pago(cliente, monto, moneda, tipo, fecha)
    pagos.append(pago)

# Función para buscar pagos por cliente
def buscar_por_cliente():
    cliente = input("Ingrese el nombre del cliente: ")
    resultados = []
    for pago in pagos:
        if pago.cliente == cliente:
            resultados.append(pago)
    if len(resultados) == 0:
        print("No se encontraron pagos para el cliente especificado.")
    else:
        print("Se encontraron los siguientes pagos para el cliente", cliente)
        for pago in resultados:
            print("- Monto:", pago.monto, pago.moneda, "- Tipo:", pago.tipo, "- Fecha:", pago.fecha)

# Función para buscar pagos por fecha
def buscar_por_fecha():
    fecha = input("Ingrese la fecha en formato DD/MM/AAAA: ")
    resultados = []
    for pago in pagos:
        if pago.fecha == fecha:
            resultados.append(pago)
    if len(resultados) == 0:
        print("No se encontraron pagos para la fecha especificada.")
    else:
        print("Se encontraron los siguientes pagos para la fecha", fecha)
        for pago in resultados:
            print("- Cliente:", pago.cliente, "- Monto:", pago.monto, pago.moneda, "- Tipo:", pago.tipo)

# Función para buscar pagos por tipo de pago
def buscar_por_tipo():
    tipo = input("Ingrese el tipo de pago (e.g. PdV, PM, Zelle, Cash): ")
    resultados = []
    for pago in pagos:
        if pago.tipo == tipo:
            resultados.append(pago)
    if len(resultados) == 0:
        print("No se encontraron pagos para el tipo de pago especificado.")
    else:
        print("Se encontraron los siguientes pagos para el tipo de pago", tipo)
        for pago in resultados:
            print("- Cliente:", pago.cliente, "- Monto:", pago.monto, pago.moneda, "- Fecha:", pago.fecha)

# Función para buscar pagos por moneda
def buscar_por_moneda():
    moneda = input("Ingrese la moneda del pago: ")
    resultados = []
    for pago in pagos:
        if pago.moneda == moneda:
            resultados.append(pago)
    if len(resultados) == 0:
        print("No se encontraron pagos para la moneda especificada.")
    else:
        print("Se encontraron los siguientes pagos para la moneda", moneda)
        for pago in resultados:
            print("- Cliente:", pago.cliente, "- Monto:", pago.monto, "- Tipo:", pago.tipo, "- Fecha:", pago.fecha)

# Menú de opciones
while True:
    print("          -------- [ Menú ] --------          \n")
    print("     1. Registrar un pago")
    print("     2. Buscar pagos por cliente")
    print("     3. Buscar pagos por fecha")
    print("     4. Buscar pagos por tipo de pago")
    print("     5. Buscar pagos por moneda")
    print("     6. Salir")
    opcion = input("     Ingrese el número de opción deseada: ")

    if opcion == "1":
        registrar_pago()
    elif opcion == "2":
        buscar_por_cliente()
    elif opcion == "3":
        buscar_por_fecha()
    elif opcion == "4":
        buscar_por_tipo()
    elif opcion == "5":
        buscar_por_moneda()
    elif opcion == "6":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del menú.")




