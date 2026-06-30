import archivo_csv
import gestion_paises
import estadisticas



def mostrar_menu():
    # ====================================================================
    # Muestra el menú principal de opciones en la consola.
    # ====================================================================
    print("\n"+"="*50)
    print("SISTEMA DE GESTIÓN DE PAÍSES")
    print("="*50)
    print("1. Agregar país")
    print("2. Buscar país por nombre")
    print("3. Actualizar población y superficie")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Guardar y salir")
    print("0. Salir sin guardar")
    print("="*50)


def buscar_y_mostrar_paises(lista_paises):
    # ====================================================================
    # Pide un término de búsqueda, busca países que coincidan y los
    # muestra en pantalla.
    # 
    # Devuelve la lista de resultados (puede estar vacía).
    # ====================================================================

    termino = input("\nIngresá el nombre o parte del nombre a buscar: ")
    resultados = gestion_paises.buscar_pais(lista_paises, termino)
    
    if resultados:
        print(f"\n--- Resultados encontrados ({len(resultados)}) ---")
        for i, pais in enumerate(resultados, 1):
            print(f"{i}. {pais['nombre']} - Población: {pais['poblacion']:,} - "
                  f"Superficie: {pais['superficie']:,} km² - Continente: {pais['continente']}")
    else:
        print(f"\nNo se encontraron países que contengan '{termino}'.")
    
    return resultados



def seleccionar_pais_de_lista(resultados):
    # ====================================================================
    # Dada una lista de países (resultados de búsqueda), permite al
    # usuario seleccionar uno mostrando un menú numerado.
    #
    # Devuelve el diccionario del país seleccionado, o None si la
    # lista está vacía o el usuario cancela.
    # ====================================================================

    if not resultados:
        return None
    
    print("\n0. Cancelar")
    while True:
        try:
            opcion = int(input(f"Seleccioná el país (1-{len(resultados)}): "))
            if opcion == 0:
                return None
            if 1 <= opcion <= len(resultados):
                return resultados[opcion - 1]
            else:
                print(f"Error: elegí un número entre 1 y {len(resultados)}")
        except ValueError:
            print("Error: ingresá un número válido")



def menu_filtros(lista_paises):
    # ====================================================================
    # Submenú para filtrar países según diferentes criterios.
    # ====================================================================
    while True:
        print("\n--- FILTRAR PAÍSES ---")
        print("1. Filtrar por continente")
        print("2. Filtrar por rango de población")
        print("3. Filtrar por rango de superficie")
        print("0. Volver al menú principal")
        
        opcion = input("\nElegí una opción: ").strip()
        
        if opcion == "1":
            continente = input("Ingresá el continente: ").strip()
            if continente:
                resultados = gestion_paises.filtrar_por_continente(lista_paises, continente)
                gestion_paises.mostrar_resultados_filtro(resultados, f"Continente: {continente}")
            else:
                print("Error: el continente no puede estar vacío.")
        
        elif opcion == "2":
            try:
                min_pob = input("Población mínima (Enter para omitir): ").strip()
                max_pob = input("Población máxima (Enter para omitir): ").strip()
                
                min_pob = int(min_pob) if min_pob else None
                max_pob = int(max_pob) if max_pob else None
                
                resultados = gestion_paises.filtrar_por_poblacion(lista_paises, min_pob, max_pob)
                gestion_paises.mostrar_resultados_filtro(resultados, "Rango de población")
            except ValueError:
                print("Error: la población debe ser un número entero.")
        
        elif opcion == "3":
            try:
                min_sup = input("Superficie mínima (km²) (Enter para omitir): ").strip()
                max_sup = input("Superficie máxima (km²) (Enter para omitir): ").strip()
                
                min_sup = int(min_sup) if min_sup else None
                max_sup = int(max_sup) if max_sup else None
                
                resultados = gestion_paises.filtrar_por_superficie(lista_paises, min_sup, max_sup)
                gestion_paises.mostrar_resultados_filtro(resultados, "Rango de superficie")
            except ValueError:
                print("Error: la superficie debe ser un número entero.")
        
        elif opcion == "0":
            break
        
        else:
            print("Error: opción inválida")



def menu_ordenamiento(lista_paises):
    # ====================================================================
    # Submenú para ordenar países según diferentes criterios.
    # ====================================================================
    print("\n--- ORDENAR PAÍSES ---")
    print("1. Ordenar por nombre")
    print("2. Ordenar por población")
    print("3. Ordenar por superficie")
    
    criterio = input("\nElegí un criterio: ").strip()
    
    if criterio not in ["1", "2", "3"]:
        print("Error: criterio inválido")
        return
    
    ascendente_input = input("¿Orden ascendente? (s/n): ").strip().lower()
    ascendente = ascendente_input == "s"
    
    # Mapear opción a clave del diccionario
    mapa_criterios = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    clave = mapa_criterios[criterio]
    
    lista_ordenada = gestion_paises.ordenar_paises(lista_paises, clave, ascendente)
    
    if lista_ordenada is None:
        print("Error: no se pudo ordenar la lista.")
        return
    
    print(f"\n--- Países ordenados por {clave} ({'ascendente' if ascendente else 'descendente'}) ---")
    for i, pais in enumerate(lista_ordenada, 1):
        if clave == "nombre":
            print(f"{i}. {pais['nombre']}")
        elif clave == "poblacion":
            print(f"{i}. {pais['nombre']} - Población: {pais['poblacion']:,}")
        else:
            print(f"{i}. {pais['nombre']} - Superficie: {pais['superficie']:,} km²")



def main():
    # ====================================================================
    # Función principal del programa.
    # Coordina la carga inicial, el bucle del menú y la ejecución de
    # todas las funcionalidades.
    # ====================================================================
    
    print("=" * 50)
    print("INICIANDO SISTEMA DE GESTIÓN DE PAÍSES")
    print("=" * 50)
    
    # Cargar datos desde el archivo CSV
    paises = archivo_csv.cargar_paises("paises.csv")
    print(f"Se cargaron {len(paises)} países desde el archivo.")
    
    datos_modificados = False  # Bandera para saber si hay cambios sin guardar
    
    # Bucle principal del menú
    while True:
        mostrar_menu()
        opcion = input("\nElegí una opción: ").strip()
        
        # Opción 1: Agregar país
        if opcion == "1":
            gestion_paises.agregar_pais(paises)
            datos_modificados = True
        
        # Opción 2: Buscar país
        elif opcion == "2":
            buscar_y_mostrar_paises(paises)
        
        # Opción 3: Actualizar país
        elif opcion == "3":
            print("\n--- Actualizar país ---")
            print("Primero buscá el país que querés modificar:")
            resultados = buscar_y_mostrar_paises(paises)
            pais_a_actualizar = seleccionar_pais_de_lista(resultados)
            
            if pais_a_actualizar:
                gestion_paises.actualizar_pais(pais_a_actualizar)
                datos_modificados = True
        
        # Opción 4: Filtrar países
        elif opcion == "4":
            menu_filtros(paises)
        
        # Opción 5: Ordenar países
        elif opcion == "5":
            menu_ordenamiento(paises)
        
        # Opción 6: Mostrar estadísticas
        elif opcion == "6":
            estadisticas.mostrar_todas_estadisticas(paises)
        
        # Opción 7: Guardar y salir
        elif opcion == "7":
            if datos_modificados:
                archivo_csv.guardar_paises(paises, "paises.csv")
            print("¡Hasta luego!")
            break
        
        # Opción 0: Salir sin guardar
        elif opcion == "0":
            if datos_modificados:
                confirmar = input("Hay cambios sin guardar. ¿Salir sin guardar? (s/n): ").strip().lower()
                if confirmar == "s":
                    print("¡Hasta luego!")
                    break
                else:
                    print("Podés guardar los cambios con la opción 7.")
            else:
                print("¡Hasta luego!")
                break
        
        else:
            print("Error: opción inválida. Elegí un número del 0 al 7.")



# Punto de entrada del programa
if __name__ == "__main__":
    main()