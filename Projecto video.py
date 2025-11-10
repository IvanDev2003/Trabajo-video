import csv

talleres = []

def agregar_taller(taller):
    nombre = input("Ingrese el nombre del taller: ")
    cupo_maximo = int(input("Ingrese el cupo maximo del taller: "))
    inscritos = int(input("Ingrese la cantidad de inscritos al taller: "))

    taller = {
        "nombre": nombre,
        "cupo maximo": cupo_maximo,
        "inscritos": inscritos
    }
    talleres.append(taller)
    print("Taller agregado con exito.")

def mostrar_talleres(talleres):
    if not talleres:
        print("no hay talleres disponibles.")
    else:
        print(talleres)

def eliminar_taller(talleres):
    nombre = input("Ingrese el nombre del taller a eliminar: ")
    for taller in talleres:
        if taller["nombre"] == nombre:
            talleres.remove(taller)
            print("Taller eliminado con exito.")
            return
    print("Taller no encontrado.")

def modificar_taller(talleres):
    nombre = input("Ingrese el nombre del taller a modificar: ")
    for taller in talleres:
        if taller["nombre"] == nombre:
            nuevo_nombre = input("Ingrese el nuevo nombre del taller: ")
            nuevo_cupo = int(input("Ingrese el nuevo cupo maximo del taller: "))
            nuevo_inscritos = int(input("Ingrese la nueva cantidad de inscritos al taller: "))
            
            taller["nombre"] = nuevo_nombre
            taller["cupo maximo"] = nuevo_cupo
            taller["inscritos"] = nuevo_inscritos
            
            print("Taller modificado con exito.")
            return
    print("Taller no encontrado.")

def exportar_talleres_a_csv(talleres, Listado_de_talleres):
    with open(Listado_de_talleres, mode='w', newline='') as archivo_csv:
        campos = ['nombre', 'cupo maximo', 'inscritos']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        for taller in talleres:
            escritor_csv.writerow(taller)
    print(f"Talleres exportados a {Listado_de_talleres} exitosamente.")

def importar_talleres_de_csv(Listado_de_talleres):
    with open(Listado_de_talleres, mode='r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            taller = {
                "nombre": fila['nombre'],
                "cupo maximo": int(fila['cupo maximo']),
                "inscritos": int(fila['inscritos'])
            }
            talleres.append(taller)
    print(f"Talleres importados de {Listado_de_talleres} exitosamente.")

def buscar_taller(talleres, nombre):
    for taller in talleres:
        if taller["nombre"] == nombre:
            return taller
    return None

def main():
    while True:
        print("\nMenu:")
        print("1. Agregar Taller")
        print("2. Mostrar Talleres")
        print("3. Eliminar Taller")
        print("4. Modificar Taller")
        print("5. Descargar talleres a CSV")
        print("6. Importar talleres de CSV")
        print("7. Buscar Taller")
        print("8. Salir")

        opcion = input("seleccione una opcion: ")

        if opcion == "1":
            agregar_taller(talleres)
        elif opcion == "2":
            mostrar_talleres(talleres)
        elif opcion == "3":
            eliminar_taller(talleres)
        elif opcion == "4":
            modificar_taller(talleres)
        elif opcion == "5":
            exportar_talleres_a_csv(talleres, 'Listado_de_talleres.csv')
        elif opcion == "6":
            importar_talleres_de_csv('Listado_de_talleres.csv')
        elif opcion == "7":
            nombre = input("Ingrese el nombre del taller a buscar: ")
            taller = buscar_taller(talleres, nombre)
            if taller:
                print("Taller encontrado:", taller)
            else:
                print("Taller no existe o no encontrado.")
        elif opcion == "8":
            print("Saliendo del programa.")
            break
        else:
            print("Ingresa una opcion valida.")

if __name__ == "__main__":
    main()
