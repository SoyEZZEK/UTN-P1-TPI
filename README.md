# Sistema de Gestión de Datos de Países

## Descripción del Proyecto

Aplicación en Python que permite gestionar información sobre países, aplicando listas, diccionarios, funciones, estructuras condicionales y repetitivas, ordenamientos y estadísticas. El sistema puede leer datos desde un archivo CSV, realizar consultas y generar indicadores clave a partir del dataset.

## Datos Institucionales

- **Institución**: Universidad Tecnológica Nacional (UTN)
- **Carrera**: Tecnicatura Universitaria en Programación a Distancia (TUPaD)
- **Materia**: Programación 1
- **Comisión**: N°7

## Integrantes

- Lautaro Ezequiel Pérez.

## Estructura del Proyecto

```
UTN-P1-TPI/
├── documentacion/
│   └── TPI_Informe.pdf          # Informe técnico del trabajo
├── proyecto-paises/
│   ├── main.py                  # Código principal
│   ├── archivo_csv.py           # Lectura/escritura CSV
│   ├── gestion_paises.py        # Lógica de negocio
│   ├── estadisticas.py          # Cálculos estadísticos
│   └── paises.csv               # Dataset de ejemplo
└── README.md                    # (Este archivo de documentación)
```

## Requisitos del Sistema

- Python 3.x (recomendado: Python 3.8 o superior)
- No requiere librerías externas (solo módulos de la biblioteca estándar: `csv`)

## Instrucciones de Ejecución

### 1. Clonar o descargar el repositorio

```bash
git clone https://github.com/tuusuario/UTN-P1-TPI.git
cd UTN-P1-TPI/proyecto-paises
```

### 2. Ejecutar el programa

```bash
python main.py
```

### 3. Navegar por el menú

```bash
==================================================
SISTEMA DE GESTIÓN DE PAÍSES
==================================================
1. Agregar país
2. Buscar país por nombre
3. Actualizar población y superficie
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Guardar y salir
0. Salir sin guardar
==================================================
```

## Ejemplos de uso

### Ejemplo 1: Agregar un país

```
--- Agregar nuevo país ---
Nombre del país: Chile
Población: 19600000
Superficie (km^2): 756102
Continente: América
País 'Chile' agregado correctamente.
```

### Ejemplo 2: Buscar país (coincidencia parcial)

```
--- Buscar país ---
Ingresá el nombre o parte del nombre a buscar: Ch

--- Resultados encontrados (1) ---
1. Chile - Población: 19,600,000 - Superficie: 756,102 km² - Continente: América
```

### Ejemplo 3: Filtrar por rango de población

```
--- FILTRAR PAÍSES ---
1. Filtrar por continente
2. Filtrar por rango de población
3. Filtrar por rango de superficie

Elegí una opción: 2

Población mínima (Enter para omitir): 50000000
Población máxima (Enter para omitir): 200000000

--- Resultados del filtro: Rango de población (2 países) ---
1. Japón - Población: 125,800,000 - Superficie: 377,975 km² - Continente: Asia
2. Alemania - Población: 83,149,300 - Superficie: 357,022 km² - Continente: Europa
```

## Validaciones Implementadas

```
Campos vacíos                No se permiten al agregar un país
Tipo de dato numérico        Población y superficie deben ser números enteros
CSV mal formado              Se omiten filas con errores y se informa al usuario
Búsquedas sin resultados     Mensaje claro indicando que no se encontraron coincidencias
Filtros inválidos            Se validan rangos numéricos antes de aplicar
Archivo CSV inexistente      Se crea uno nuevo o se informa el error
```

## Enlace al vídeo

Video demostrativo: https://youtu.be/ENLACE-AL-VÍDEO
