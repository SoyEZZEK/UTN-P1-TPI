def pais_mayor_poblacion(lista_paises):
    # ====================================================================
    # Devuelve el diccionario del país con mayor población.
    # Si la lista está vacía, devuelve None.
    # ====================================================================

    if not lista_paises:
        return None
    
    pais_max = lista_paises[0]
    for pais in lista_paises:
        if pais["poblacion"] > pais_max["poblacion"]:
            pais_max = pais
    
    return pais_max



def pais_menor_poblacion(lista_paises):
    # ====================================================================
    # Devuelve el diccionario del país con menor población.
    # Si la lista está vacía, devuelve None.
    # ====================================================================

    if not lista_paises:
        return None
    
    pais_min = lista_paises[0]
    for pais in lista_paises:
        if pais["poblacion"] < pais_min["poblacion"]:
            pais_min = pais
    
    return pais_min



def promedio_poblacion(lista_paises):
    # ====================================================================
    # Calcula y devuelve el promedio de población de todos los países.
    # Si la lista está vacía, devuelve 0.
    # ====================================================================

    if not lista_paises:
        return 0
    
    suma = 0
    for pais in lista_paises:
        suma += pais["poblacion"]
    
    return suma / len(lista_paises)



def promedio_superficie(lista_paises):
    # ====================================================================
    # Calcula y devuelve el promedio de superficie de todos los países.
    # Si la lista está vacía, devuelve 0.
    # ====================================================================

    if not lista_paises:
        return 0
    
    suma = 0
    for pais in lista_paises:
        suma += pais["superficie"]
    
    return suma / len(lista_paises)



def cantidad_por_continente(lista_paises):
    # ====================================================================
    # Devuelve un diccionario donde las claves son los continentes
    # y los valores son la cantidad de países en cada uno.
    # ====================================================================

    contador = {}
    
    for pais in lista_paises:
        continente = pais["continente"]
        if continente in contador:
            contador[continente] += 1
        else:
            contador[continente] = 1
    
    return contador



def mostrar_todas_estadisticas(lista_paises):
    # ====================================================================
    # Muestra en pantalla todas las estadísticas calculadas.
    # ====================================================================

    if not lista_paises:
        print("\nNo hay países cargados para mostrar estadísticas.")
        return
    
    print("\n"+"="*50)
    print("ESTADÍSTICAS DE PAÍSES")
    print("="*50)
    
    # País con mayor población
    max_pob = pais_mayor_poblacion(lista_paises)
    if max_pob:
        print(f"\n- País con MAYOR población:")
        print(f"    {max_pob['nombre']} - {max_pob['poblacion']:,} habitantes")
    
    # País con menor población
    min_pob = pais_menor_poblacion(lista_paises)
    if min_pob:
        print(f"\n- País con MENOR población:")
        print(f"    {min_pob['nombre']} - {min_pob['poblacion']:,} habitantes")
    
    # Promedio de población
    prom_pob = promedio_poblacion(lista_paises)
    print(f"\n- Promedio de población: {prom_pob:,.0f} habitantes")
    
    # Promedio de superficie
    prom_sup = promedio_superficie(lista_paises)
    print(f"\n- Promedio de superficie: {prom_sup:,.0f} km²")
    
    # Cantidad de países por continente
    print("\n- Cantidad de países por continente:")
    contador = cantidad_por_continente(lista_paises)
    for continente, cantidad in sorted(contador.items()):
        print(f"    {continente}: {cantidad} país(es)")
    
    print("\n"+"="*50)