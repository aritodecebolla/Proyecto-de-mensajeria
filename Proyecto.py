import os
import random

nombre_archivo = "usuarios.txt"
archivo_guia = "guia.txt"
archivo_paquetes="paquetes.txt"
lista_usuarios = []

def limpiar_pantalla():
    if os.name == "posix":  # Unix/Linux/MacOS/BSD
        os.system("clear")
    elif os.name == "nt":  # Windows
        os.system("cls")
    else:
        print("\n" * 100)

def mostrar_menu():
    print("Menu de Ingreso\n")
    print("1 - Crear Usuario")
    print("2 - Login")
    print("3 - Salir\n")


def mostrar_menu_servicios(usuario):
    while True:
        limpiar_pantalla()
        print(f"Menu de Servicios   usuario:{usuario[0]}\n")
        print("1 - Crear Guía")
        print("2 - Crear Paquete")
        print("3 - Enviar Paquete")
        print("4 - Rastrear Paquete")
        print("5 - Estadistica de usuario")
        print("6 - Salir\n")
        opcion = input("Digite una opción: ")
        if opcion == "1":
            mostrar_menu_guia(usuario)
        elif opcion == "2":
            mostrar_menu_paquete()
        elif opcion == "3":
            envia_paquete()    
        elif opcion == "6":
            break

def envia_paquete():
    datos=[]
    limpiar_pantalla()
    guia=input("Digite el número de guía del paquete a enviar:")
    with open(archivo_paquetes, "r") as archivo:
        lineas = archivo.readlines()
        

    linea_encontrada = False
    for i, linea in enumerate(lineas):
        if guia == linea[0]:
            datos = linea.strip().split(',')
            datos[7] = "Enviado"  # Modificamos el estado del paquete
            lineas[i] = ','.join(datos[:8]) +  "\n"  # Convertimos la lista en una cadena de texto
            linea_encontrada = True
            break

    if linea_encontrada:
        with open(archivo_paquetes, "w") as archivo:
            archivo.writelines(lineas)
        print("Se Envio el paquete.")
        input("...")
    else:
        print(f"No se encontró el numero de guía '{guia}' en los paquetes.")
        input("...")

def mostrar_menu_paquete():
    while True:
        limpiar_pantalla()
        print("Creación de paquete\n")
        print("1 - Crear paquete")
        print("2 - Salir\n")
        opcion = input("Digite una opción: ")
        if opcion == "1":
            crea_paquete()
        elif opcion == "2":
            break

def busca_guia(guia):
    datos=[]
    with open(archivo_guia, 'r') as archivo:
        for linea in archivo:
            f_guia=linea.strip().split(',')[0]
            datos=linea.strip().split(',')
            if f_guia == guia:
                return datos
    print("Numero de guia no existe.")
    input("Presione una tecla para continuar...")
    return False

def guarda_paquete(datos):
    limpiar_pantalla()
    # Verificar si el usuario ya existe en el archivo
    if paquete_existe(archivo_paquetes):
        with open(archivo_paquetes, 'a+') as archivo:
            # Agregar el usuario al archivo
            archivo.write(f"{datos[0]},{datos[1]},{datos[2]},{datos[3]},{datos[4]},{datos[5]},{datos[6]},{datos[7]},Creado\n")
            print("El paquete ha sido creado.")
    else:
        # Abrir el archivo en modo de apertura ('a+')
        with open(archivo_paquetes, 'w') as archivo:
            # Agregar el usuario al archivo
            archivo.write(f"{datos[0]},{datos[1]},{datos[2]},{datos[3]},{datos[4]},{datos[5]},{datos[6]},{datos[7]},Creado\n")
            print("El paquete ha sido creado.")

def crea_paquete():
    limpiar_pantalla()
    datos=[]
    print("Creación de paquete\n")
    guia = input("Digite el numero de guía: ")
    print("\n")
    datos=busca_guia(guia)
    if datos != False:
        print(f"Destinatario: {datos[3]}")
        print(f"Teléfono: {datos[4]}")
        cedula = input("Digite el numero de cédula del destinatario: ")
        peso = input("Digite el peso del paquete: ")
        print(f"Cobro: {datos[5]}\n")
        respuesta = input("Desea Guardar el paquete? (S/N): ")
        if respuesta=="S":
            datos.append(cedula)
            datos.append(peso)
            datos.append("Creado")
            guarda_paquete(datos)
            return True
        else:
            print("\n")
            print("Paquete no creado.\n")
            input("Presione una tecla para continuar...")
            return False
    else:
        print("\n")
        print(f"No se encontró el número de guia: {guia}")
        input("Presione una tecla para continuar...")
        return False
    
def genera_guia(datos):
    guia=random.randrange(1, 9999999999, 1)    
    with open(archivo_guia, 'w') as archivo:
        archivo.write(f"{guia},{datos[3]},{datos[4]},{datos[7]},{datos[8]},{datos[9]}\n")
    return guia

def mostrar_menu_guia(usuario):
    destinatario=""
    telefono=""
    cobro=""
    datos=[]
    while True:
        limpiar_pantalla()
        print("Creación de guía\n")
        print("1 - Crear guía")
        print("2 - Eliminar guía")
        print("3 - Salir\n")
        opcion = input("Digite una opción: ")
        if opcion == "1":
            datos=carga_datos_usuario(nombre_archivo,usuario)
            destinatario=input("Digite el nombre del destinatario:")
            telefono=input("Digite el telefono del destinatario:")
            cobro=input("Digite el monto a cobrar o déjelo en blanco:")
            print("\n")
            print("\n")
            print("Impresión de Guía\n")
            print(f"Comercio remitente: {datos[3]}")
            print(f"Teléfono: {datos[4]}\n")
            print(f"Nombre del destinatario: {destinatario}")
            print(f"Teléfono del destinatario: {telefono}")
            print(f"Monto a cobrar: {cobro}")
            datos.append(destinatario)
            datos.append(telefono)
            datos.append(cobro)
            guia=genera_guia(datos)
            print(f"Guia Generada #:{guia}\n")
            input("Presione una tecla para continuar...")
            break
        elif opcion == "2":
            os.remove(nombre_archivo)
            print("Archivo de guias eliminado.\n")
            input("Presione una tecla para continuar...")
        elif opcion == "3":
            break

def paquete_existe(archivo_paquete):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return True
        return False
    except FileNotFoundError:
        return False
    
def usuario_existe(nombre_archivo, usuario):
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                if f"{usuario[0]}" in linea.strip().split(',')[0]:
                    return True
        return False
    except FileNotFoundError:
        return False

def guardar_usuario_en_archivo(nombre_archivo, usuario):
    limpiar_pantalla()
    # Verificar si el usuario ya existe en el archivo
    if usuario_existe(nombre_archivo, usuario):
        print(f"El usuario '{usuario[0]}' ya existe en el archivo.")
    else:
        # Abrir el archivo en modo de apertura ('a+')
        with open(nombre_archivo, 'a+') as archivo:
            # Agregar el usuario al archivo
            archivo.write(f"{usuario[0]},{usuario[1]},{usuario[2]},{usuario[3]},{usuario[4]},{usuario[5]},{usuario[6]}\n")
            print(f"El usuario '{usuario[0]}' ha sido agregado al archivo.")

def crear_usuario():
    # Solicitar los datos del usuario
    nombre = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña: ")
    correo = input("Ingrese el correo del comercio: ")
    comercio = input("Ingrese el nombre del comercio: ")
    telefono = input("Ingrese el teléfono del comercio: ")
    propietario = input("Ingrese el nombre del propietario: ")
    ubicacion = input("Ingrese la ubicación del comercio: ")

    usuario = (nombre, contrasena, correo, comercio, telefono, propietario, ubicacion)
    guardar_usuario_en_archivo(nombre_archivo, usuario)

def valida_usuario(nombre_archivo, usuario):
    nombre_usuario = usuario[0]
    contrasena = usuario[1]
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            f_usuario=linea.strip().split(',')[0]
            f_contrasena=linea.strip().split(',')[1]
            if f_usuario == nombre_usuario and f_contrasena== contrasena:
                print(f"Usuario '{nombre_usuario}' y contraseña son correctos.")
                return True
    print(f"Usuario '{nombre_usuario}' o contraseña incorrectos.")
    input("Presione una tecla para continuar...")
    return False

def carga_datos_usuario(nombre_archivo,usuario):
    f_usuario=usuario[0]
    datos_linea=[]
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            datos_linea = linea.strip().split(',')
            if datos_linea[0] ==f_usuario:
                return datos_linea
    print(f"Usuario '{usuario}' no se encuentra.")
    input("Presione una tecla para continuar...")
    return False

    
def mostrar_loggin():
    
    print("Loggin\n")
    nombre = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña: ")
    print("\n")
    usuario = (nombre, contrasena)
    if valida_usuario(nombre_archivo, usuario):
            mostrar_menu_servicios(usuario)
            
while True:
    mostrar_menu()
    opcion = input("Digite una opción: ")

    if opcion == "1":
        limpiar_pantalla()
        print("Ha seleccionado Crear Usuario.")
        crear_usuario()
        input("Presione una tecla para continuar...")
        limpiar_pantalla()
    elif opcion == "2":
        limpiar_pantalla()
        mostrar_loggin()
        limpiar_pantalla()
    elif opcion == "3":
        break
    else:
        limpiar_pantalla()
        print("Opción no válida. Por favor, elija una opción válida.")
        input("Presione una tecla para continuar...")
        limpiar_pantalla()
