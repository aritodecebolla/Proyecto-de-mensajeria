# Función para rastrear el estado del paquete
def rastrear_paquete(numeroGuia):
    if numeroGuia in paquetes_estado:
        return paquetes_estado[numeroGuia]
    else:
        return "Número de guía no encontrado. Verifique el número ingresado."

paquetes_estado=int(input("Seleccione 1 si desea ver el estado del paquete, y 2 si no la desea:"))
if paquetes_estado==1:
  # Rastreo del paquete
  numero_guia_rastreo = input("Ingrese el número de guía del paquete a rastrear: ")
  estado_actual = rastrear_paquete(numero_guia_rastreo)
  print(f"El estado actual del paquete con número de guía {numero_guia_rastreo} es: {estado_actual}")

