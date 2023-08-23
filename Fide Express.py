import os
import random
import re

nombre_archivo = "usuarios.txt"
archivo_guia = "guia.txt"
archivo_paquetes="paquetes.txt"
lista_usuarios = []

def es_correo_valido(correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, correo))

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
    
def rastrea_paquete():
    limpiar_pantalla()
    print("Rastreo de paquete\n")
    guia=input("Digite el número del paquete(#guía) a rastrear: ")
    with open(archivo_paquetes, 'r') as archivo:
        for linea in archivo:
            f_guia=linea.strip().split(',')[0]
            estado=linea.strip().split(',')[8]
            if f_guia == guia:
                print("\n")
                print(f"El paquete con el numero de guia: '{guia}' tiene el estado de: {estado}")
                input("Digite una tecla para continuar...")
                return True
    print(f"Problema al leer el archivo.")
    return False

def p_enviados():
    try:
        limpiar_pantalla()
        cantidad=0
        print ("Lista de Paquetes enviados\n")
        with open(archivo_paquetes, 'r') as archivo:
            for linea in archivo:
                datos=linea.strip().split(',')
                estado=linea.strip().split(',')[8]
                if estado=="Enviado":
                    print(f"Numero de paquete: {datos[0]}\n")
                    print(f"     Destinatario: {datos[3]}\n")
                    print(f"     Teléfono del destinatario: {datos[4]}\n")
                    print(f"     Cédula Destinatario: {datos[6]}\n")
                    print(f"     Peso del paquete: {datos[7]}\n")
                    print(f"     Precio: {datos[5]}\n")
                    print("\n\n")
        input ("Digite una tecla para continuar...")
    except FileNotFoundError:
        print (f"Problemas al abrir el archivo {archivo_paquetes}\n")
        input ("Digite una tecla para continuar...")    

def c_envios(usuario):
    try:
        limpiar_pantalla()
        print ("Cantidad de envíos\n")
        cantidad=0
        with open(archivo_paquetes, 'r') as archivo:
            for linea in archivo:
                cantidad=cantidad+1
        print(f"La cantidad de paquetes enviados por el usuario {usuario[0]} es de {cantidad}")
        input ("Digite una tecla para continuar...")
    except FileNotFoundError:
        print (f"Problemas al abrir el archivo {archivo_paquetes}\n")
        input ("Digite una tecla para continuar...")

def m_total():
    try:
        limpiar_pantalla()
        m_cobrado=0
        print ("Monto total de paquetes\n")
        with open(archivo_paquetes, 'r') as archivo:
            for linea in archivo:
                cobrado=linea.strip().split(',')[5]
                m_cobrado=float(m_cobrado)+ float(cobrado)
            print(f"El monto total cobrado de los paquetes es de: {m_cobrado}")
            input ("Digite una tecla para continuar...")
    except FileNotFoundError:
        print (f"Problemas al abrir el archivo {archivo_paquetes}\n")
        input ("Digite una tecla para continuar...")  

def p_telefono(opcion,usuario):
    try:
        limpiar_pantalla()
        if opcion=="T":
            print ("Cantidad de envíos por telefono de destinatario\n\n")
            dato=input("Digite el numero de telefono a consultar: ")
            tipo="teléfono"
        elif opcion=="C":
            print ("Cantidad de envíos por cédula de destinatario\n\n")
            dato=input("Digite el numero de cédula a consultar: ")
            tipo="cédula"
        cantidad=0
        print("\n\n")
        with open(archivo_paquetes, 'r') as archivo:
            for linea in archivo:
                if opcion=="T": 
                    f_dato=linea.strip().split(',')[4]
                elif opcion=="C":
                    f_dato=linea.strip().split(',')[6]
                if dato==f_dato:
                    cantidad=cantidad+1
        print(f"La cantidad de paquetes enviados por el usuario {usuario[0]} por {tipo}:{dato} es de {cantidad}")
        input ("Digite una tecla para continuar...")
    except FileNotFoundError:
        print (f"Problemas al abrir el archivo {archivo_paquetes}\n")
        input ("Digite una tecla para continuar...")    
    
    
def menu_estadistica(usuario):
    while True:
        #Proceso para limpiar la pantalla definido en linea 10.
        limpiar_pantalla()
        #Menu de estadisticas.
        print(f"Menu de Estadisticas   usuario:{usuario[0]}\n")
        print("1 - Cantidad de Envios")
        print("2 - Paquetes Enviados")
        print("3 - Monto Total Cobrado")
        print("4 - Cantidad de paquetes por numero de telefono")
        print("5 - Cantidad de paquetes por cédula")
        print("6 - Salir\n")
        #carga en la variable opcion  la opcion digitada por el usuario.
        opcion = input("Digite una opción: ")
        if opcion == "1":
            c_envios(usuario)
        elif opcion == "2":
            p_enviados()
        elif opcion == "3":
            m_total()
        elif opcion == "4":
            p_telefono("T",usuario)
        elif opcion == "5":
            p_telefono("C",usuario)
        elif opcion == "6":
            break
        else:
            print("Opción Inválida.")
            input("Digite una tecla para continuar...")
   
def factu_dig():
    correo=""
    #Registro de la Factura Electrónica opcional
    facturaelectro=int(input("Seleccione 1 si desea factura electrónica, y 2 si no la desea: "))
    if facturaelectro==1:
      tipodecedula=int(input("Seleccione 1 para cédula de identidad y 2 para cédula jurídica: "))
      print(tipodecedula)
      if tipodecedula==1:
        cedulaID=int(input("Digite su cédula de identidad: "))
        print(cedulaID)
      if tipodecedula==2:
        cedulajuridica=int(input("Digite la cédula jurídica: "))
        print(cedulajuridica)
      nombreregistrado=input("Digite su nombre registrado: ")
      print(nombreregistrado)
      telefonocomercio=int(input("Ingrese el número de teléfono de la compañia: "))
      print(telefonocomercio)
      while es_correo_valido(correo) ==False:
          correo=input("Ingrese su correo electrónico: ")
          if es_correo_valido(correo) ==False:
              print(correo+ ' (Correo Inválido)')
      print(correo + ' (Verificado)')  
      print("Ingrese su ubicación por: Provincia, canton y distrito: ")
      provincia=input("Provincia: ")
      print(provincia)
      canton=input("Canto: ")
      print(canton)
      distrito=input("Distrito: ")
      print(distrito)
      print(provincia,canton,distrito)

def mostrar_menu_servicios(usuario):
    while True:
        limpiar_pantalla()
        print(f"Menu de Servicios   usuario:{usuario[0]}\n")
        print("1 - Crear Guía")
        print("2 - Crear Paquete")
        print("3 - Cambiar estado")
        print("4 - Rastrear Paquete")
        print("5 - Estadistica de usuario")
        print("6 - Factura Digital")
        print("7 - Salir\n")
        opcion = input("Digite una opción: ")
        if opcion == "1":
            mostrar_menu_guia(usuario)
        elif opcion == "2":
            crea_paquete()
        elif opcion == "3":
            cambiar_estado()
        elif opcion == "4":
            rastrea_paquete()
        elif opcion == "5":
            menu_estadistica(usuario)
        elif opcion == "6":
            factu_dig()
        elif opcion == "7":
            break
        
def cambiar_estado():
    limpiar_pantalla()
    encontro = False
    guia=input("Digite el número de guía del paquete: ")
    print("\n\n")
    print("Estados: (1-Enviado,2-Entrega Fallida,3-Entregado)\n")
    opcion=input("Digite el número de estado al cual desea cambiar el paquete: ")            
    #Abre el archivo de paquetes en modo lectura.
    with open(archivo_paquetes, 'r') as f:
        lines = f.readlines()
        new_lines = []
        #Recorreo las lineas del archivo.
        for line in lines:
            fields = line.strip().split(',')
            if fields[0] == guia:
                if opcion=="1":
                    fields[8]="Enviado"
                elif opcion=="2":
                    fields[8]="Entrega Fallida"
                elif opcion=="3":
                    fields[8]="Entregado"
                encontro=True
            new_lines.append(','.join(fields)+ '\n')
        if encontro==True:
            with open('paquetes.txt', 'w') as f:
                f.writelines(new_lines)
                print("Cambio realizado.")
                input("Digite una tecla para continuar...")
                return True
            print("Error al escribir en el archivo.")
            return False
        else:
            print("No se encontró el numero de guia en el archivo.")
            input("Digite una tecla para continuar...")
            return False
    #Error solo si el with de la linea 211 no logra abrir el archivo.
    print("Error al escribir en el archivo.")
    return False

def busca_guia(guia):
    datos=[]
    with open(archivo_guia, 'r') as archivo:
        for linea in archivo:
            f_guia=linea.strip().split(',')[0]
            datos=linea.strip().split(',')
            if f_guia == guia:
                return datos
    print("No se encontro el archivo o el numero de guia es incorrecto.")
    return False

def guarda_paquete(datos):
    limpiar_pantalla()
    # Verificar si el usuario ya existe en el archivo
    if paquete_existe(archivo_paquetes):
        with open(archivo_paquetes, 'a+') as archivo:
            # Agregar el usuario al archivo
            archivo.write(f"{datos[0]},{datos[1]},{datos[2]},{datos[3]},{datos[4]},{datos[5]},{datos[6]},{datos[7]},Creado\n")
            print("El paquete ha sido creado.")
            input("Presione una tecla para continuar...")
    else:
        # Abrir el archivo en modo de apertura ('w')
        with open(archivo_paquetes, 'w') as archivo:
            # Agregar el usuario al archivo
            archivo.write(f"{datos[0]},{datos[1]},{datos[2]},{datos[3]},{datos[4]},{datos[5]},{datos[6]},{datos[7]},Creado\n")
            print("El paquete ha sido creado.")
            input("Presione una tecla para continuar...")

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
        peso = input("Digite el peso del paquete en kilos: ")
        calculo = float (peso) * float (datos[5])
        print(f"Cobro: {calculo}\n")
        respuesta = input("Desea Guardar el paquete? (S/N): ")
        if respuesta.upper()=="S":
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
            print(f"Monto a cobrar por kilo: {cobro}")
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
        print(f"El usuario '{usuario[0]}' con nombre completo '{usuario[1]}' ya existe en el archivo.")
    else:
        # Abrir el archivo en modo de apertura ('a+')
        with open(nombre_archivo, 'a+') as archivo:
            # Agregar el usuario al archivo
            archivo.write(f"{usuario[0]},{usuario[1]},{usuario[2]},{usuario[3]},{usuario[4]},{usuario[5]},{usuario[6]}\n")
            print(f"El usuario '{usuario[0]}' ha sido agregado al archivo.")

def crear_usuario():
    correo=""
    # Solicitar los datos del usuario
    nombre = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña: ")
    while es_correo_valido(correo) ==False:
        correo = input("Ingrese el correo del comercio: ")
        if es_correo_valido(correo) ==False:
            print(correo+ ' (Correo Inválido)')
    print(correo + ' (Verificado)')  
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
    limpiar_pantalla()
    if opcion == "1":
        print("Ha seleccionado Crear Usuario.")
        crear_usuario()
        input("Presione una tecla para continuar...")
    elif opcion == "2":
        mostrar_loggin()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        input("Presione una tecla para continuar...")
    limpiar_pantalla()
    

        
