import csv

def cargar_paises(ruta_csv="paises.csv"):
    # ====================================================================
    # Lee el archivo CSV y devuelve una lista de diccionarios,
    # donde cada diccionario representa un país con sus datos.

    # Si el archivo no existe o hay un error de formato en alguna fila,
    # se informa el problema y se continúa (o se devuelve una lista vacía
    # si el archivo no se puede abrir).
    # ====================================================================

    lista_paises = []

    try:
    # Abrir el archivo CSV para lectura
        with open(ruta_csv, mode="r", encoding="utf-8") as archivo: 
            # "encoding" para evitar problemas con caracteres especiales como la ñ o acentos
            lector = csv.DictReader(archivo)
            # DictReader lee el CSV y devuelve cada fila como un diccionario, usando la primera fila como claves
            # Ejemplo: {"nombre": "Argentina", 
            #           "poblacion": "45000000", 
            #           "superficie": "2780000", 
            #           "continente": "América"}

            for fila in lector:
                try: 
                # Validar y convertir los datos de cada fila
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    lista_paises.append(pais)
                except (ValueError, KeyError) as error:
                # Si hay un error de conversión o falta una columna, se omite esa fila
                    print(f"Aviso: se omitió una fila con datos inválidos ({error}).")

    except FileNotFoundError:
    # Si el archivo no se encuentra, se informa el error y se devuelve una lista vacía
        print(f"Error: no se encontró el archivo '{ruta_csv}'.")

    return lista_paises



def guardar_paises(lista_paises, ruta_csv="paises.csv"):
    # ====================================================================
    # Escribe la lista de países (lista de diccionarios) en un archivo CSV,
    # sobrescribiendo el contenido anterior.

    # Cada diccionario debe tener las claves: nombre, poblacion, superficie y continente.
    # Si ocurre un error al escribir el archivo, se informa el problema.
    # ====================================================================

    columnas = ["nombre", "poblacion", "superficie", "continente"]

    try:
    # Abrir el archivo en modo escritura ("w" sobrescribe el contenido existente)
        with open(ruta_csv, mode="w", encoding="utf-8", newline="") as archivo:
            # "newline=''" evita que se agreguen líneas vacías de más entre filas en Windows

            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            # Escribir la primera fila con los nombres de las columnas

            escritor.writeheader()
            # Escribir una fila por cada país de la lista

            for pais in lista_paises:
                escritor.writerow(pais)

        print(f"Datos guardados correctamente en '{ruta_csv}'.")

    except OSError as error:
    # Captura errores de escritura (permisos, ruta inválida, etc.)
        print(f"Error al guardar el archivo '{ruta_csv}': {error}")