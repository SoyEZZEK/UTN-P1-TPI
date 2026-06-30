def agregar_pais(lista_paises):
    # ====================================================================
    # Solicita al usuario los datos de un nuevo país y lo agrega a la
    # lista de países, siempre y cuando todos los campos sean válidos
    # y no estén vacíos.
    #
    # No se permiten campos vacíos ni valores numéricos inválidos.
    # ====================================================================

    print("\n--- Agregar nuevo país ---")

    # Pedir el nombre, para asegurar de que no quede vacío
    nombre = input("Nombre del país: ").strip()
    while nombre == "":
        print("Error: el nombre no puede estar vacío.")
        nombre = input("Nombre del país: ").strip()

    # Pedir la población, validando que sea un número entero
    poblacion = None # Inicialmente se asigna None para entrar al ciclo de validación
    while poblacion is None:
        entrada = input("Población: ").strip()
        try:
            poblacion = int(entrada)
        except ValueError:
            print("Error: ingresá un número entero válido para la población.")

    # Pedir la superficie, validando que sea un número entero
    superficie = None # Inicialmente se asigna None para entrar al ciclo de validación
    while superficie is None:
        entrada = input("Superficie (km^2): ").strip()
        try:
            superficie = int(entrada)
        except ValueError:
            print("Error: ingresá un número entero válido para la superficie.")

    # Pedir el continente, para asegurar de que no quede vacío
    continente = input("Continente: ").strip()
    while continente == "":
        print("Error: el continente no puede estar vacío.")
        continente = input("Continente: ").strip()

    # Armar el diccionario del nuevo país y se agrega a la lista
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    lista_paises.append(nuevo_pais) # Agrega el nuevo país a la lista de países

    print(f"País '{nombre}' agregado correctamente.")



def buscar_pais(lista_paises, termino_busqueda):
    # ====================================================================
    # Busca países cuyo nombre contenga el término ingresado, sin
    # distinguir entre mayúsculas y minúsculas (coincidencia parcial
    # o exacta).
    #
    # Devuelve una lista con los diccionarios de los países que
    # coinciden. Si no hay coincidencias, devuelve una lista vacía.
    # ====================================================================

    termino = termino_busqueda.strip().lower()
    # Elimina espacios y convierte aminúsculas para comparación

    resultados = []

    for pais in lista_paises:
        nombre_pais = pais["nombre"].lower()
        if termino in nombre_pais:
            resultados.append(pais)

    return resultados



def actualizar_pais(pais):
    # ====================================================================
    # Actualiza la población y la superficie de un país.
    #
    # Recibe el diccionario del país a modificar (ya identificado
    # previamente, por ejemplo: mediante buscar_pais).
    #
    # Si el usuario deja un campo vacío, se conserva el valor actual.
    # Como los diccionarios se pasan por referencia, los cambios se
    # reflejan directamente en la lista original sin necesidad de
    # devolver nada.
    # ====================================================================

    print("\n--- Actualizar país ---")
    print(f"Datos actuales de '{pais['nombre']}':")
    print(f"  Población: {pais['poblacion']}")
    print(f"  Superficie: {pais['superficie']} km^2")
    print("(Dejá el campo vacío para mantener el valor actual)")

    # Pedir nueva población
    while True:
        entrada = input("Nueva población: ").strip()
        if entrada == "":
            # El usuario no quiere cambiar este dato
            break
        try:
            pais["poblacion"] = int(entrada)
            break
        except ValueError:
            print("Error: ingresá un número entero válido o dejá vacío para mantener el actual.")

    # Pedir nueva superficie
    while True:
        entrada = input("Nueva superficie (km^2): ").strip()
        if entrada == "":
            # El usuario no quiere cambiar este dato
            break
        try:
            pais["superficie"] = int(entrada)
            break
        except ValueError:
            print("Error: ingresá un número entero válido o dejá vacío para mantener el actual.")

    print(f"País '{pais['nombre']}' actualizado correctamente.")



def filtrar_por_continente(lista_paises, continente):
    # ====================================================================
    # Filtra los países que pertenecen al continente especificado.
    # La comparación NO distingue mayúsculas/minúsculas.
    #
    # Devuelve una lista con los países que coinciden.
    # ====================================================================

    continente_busqueda = continente.strip().lower()
    resultados = []
    
    for pais in lista_paises:
        if pais["continente"].lower() == continente_busqueda:
            resultados.append(pais)
    
    return resultados



def filtrar_por_poblacion(lista_paises, min_poblacion=None, max_poblacion=None):
    # ====================================================================
    # Filtra los países cuya población esté dentro del rango especificado.
    # 
    # Parámetros:
    #   - min_poblacion: valor mínimo (incluido) o None para sin límite inferior
    #   - max_poblacion: valor máximo (incluido) o None para sin límite superior
    #
    # Devuelve una lista con los países que cumplen la condición.
    # ====================================================================

    resultados = []
    
    for pais in lista_paises:
        poblacion = pais["poblacion"]
        
        # Verificar límite inferior
        if min_poblacion is not None and poblacion < min_poblacion:
            continue
        
        # Verificar límite superior
        if max_poblacion is not None and poblacion > max_poblacion:
            continue
        
        resultados.append(pais)
    
    return resultados



def filtrar_por_superficie(lista_paises, min_superficie=None, max_superficie=None):
    # ====================================================================
    # Filtra los países cuya superficie esté dentro del rango especificado.
    # 
    # Parámetros:
    #   - min_superficie: valor mínimo (incluido) o None para sin límite inferior
    #   - max_superficie: valor máximo (incluido) o None para sin límite superior
    #
    # Devuelve una lista con los países que cumplen la condición.
    # ====================================================================

    resultados = []
    
    for pais in lista_paises:
        superficie = pais["superficie"]
        
        if min_superficie is not None and superficie < min_superficie:
            continue
        
        if max_superficie is not None and superficie > max_superficie:
            continue
        
        resultados.append(pais)
    
    return resultados



def mostrar_resultados_filtro(resultados, titulo):
    # ====================================================================
    # Muestra en pantalla los resultados de un filtro.
    # ====================================================================
    if resultados:
        print(f"\n--- Resultados del filtro: {titulo} ({len(resultados)} países) ---")
        for i, pais in enumerate(resultados, 1):
            print(f"{i}. {pais['nombre']} - Población: {pais['poblacion']:,} - "
                  f"Superficie: {pais['superficie']:,} km^2 - Continente: {pais['continente']}")
    else:
        print(f"\nNo se encontraron países que cumplan el filtro: {titulo}")



def ordenar_paises(lista_paises, clave, ascendente=True):
    # ====================================================================
    # Ordena la lista de países según la clave especificada.
    #
    # Parámetros:
    #   - lista_paises: lista original (NO se modifica)
    #   - clave: "nombre", "poblacion" o "superficie"
    #   - ascendente: True para orden ascendente, False para descendente
    #
    # Devuelve una NUEVA lista ordenada, o None si la clave es inválida.
    # ====================================================================

    try:
        return sorted(lista_paises, key=lambda pais: pais[clave], reverse=not ascendente)
    except KeyError:
        return None