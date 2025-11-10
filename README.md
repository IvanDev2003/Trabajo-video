# Sistema de Gestión de Talleres en Python

Este proyecto es un programa de consola en **Python** que permite **gestionar talleres** fácilmente.  
Puedes **agregar, modificar, eliminar, buscar y guardar talleres en archivos CSV**, además de cargarlos nuevamente cuando quieras.

---

## Características principales

 Agregar nuevos talleres  
 Mostrar todos los talleres registrados  
 Modificar o eliminar talleres existentes  
 Buscar talleres por nombre  
 Exportar e importar los datos desde un archivo CSV  
 Menú interactivo por consola  

---

## Tecnologías utilizadas

- **Python 3.x**
- Librería estándar `csv` para manejo de archivos
- Entrada y salida por consola (`input()` y `print()`)

---

## Estructura del código

El programa se compone de varias funciones principales:

| Función | Descripción |
|----------|--------------|
| `agregar_taller()` | Crea y agrega un nuevo taller a la lista. |
| `mostrar_talleres()` | Muestra todos los talleres registrados. |
| `eliminar_taller()` | Elimina un taller por su nombre. |
| `modificar_taller()` | Permite editar la información de un taller existente. |
| `exportar_talleres_a_csv()` | Guarda los talleres en un archivo CSV. |
| `importar_talleres_de_csv()` | Carga talleres desde un archivo CSV existente. |
| `buscar_taller()` | Busca un taller por su nombre. |
| `main()` | Muestra el menú principal y coordina las funciones. |

---

## Ejemplo de ejecución

Al ejecutar el programa, verás un menú como este:
