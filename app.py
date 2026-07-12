import sys
from src.agenda import agenda  # o Agenda, dependiendo de tu código
from src.busqueda_contacto import buscar_contacto

def iniciar_aplicacion():
    mi_agenda = agenda()
    
    while True:
        print("\n--- MI AGENDA TELEFÓNICA ---")
        print("1. Registrar contacto")
        print("2. Buscar contacto")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono (10 dígitos): ")
            try:
                mensaje = mi_agenda.registrar_contacto(nombre, telefono)
                print(mensaje)
            except ValueError as e:
                print(e)

        elif opcion == '2':
            nombre = input("Ingrese el nombre a buscar: ")
            try:
                mensaje = buscar_contacto(mi_agenda, nombre)
                print(mensaje)
            except ValueError as e:
                print(e)

        elif opcion == '3':
            print("Saliendo de la agenda...")
            break
            
        else:
            print("Opción no válida. Intente de nuevo.")

if _name_ == "_main_":
    iniciar_aplicacion()