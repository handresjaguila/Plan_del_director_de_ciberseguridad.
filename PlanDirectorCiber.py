# Importar librería para leer la entrada del usuario
import sys

# Definir un diccionario con subtareas correspondientes a cada opción del menú
subtasks = {
    "1": ["Revisión de políticas existentes", "Actualización de políticas obsoletas"],
    "2": ["Análisis de riesgos", "Evaluación de amenazas"],
    "3": ["Implementación de controles de acceso", "Mejoras en la seguridad de la red"],
    "4": ["Capacitación en seguridad de los empleados", "Concientización sobre phishing"],
    "5": ["Auditoría de seguridad de la red", "Pruebas de penetración"],
}

# Definir una función para mostrar el menú
def show_menu():
    print("Plan del Director de Ciberseguridad:")
    print("1. Revisión y actualización de políticas de seguridad")
    print("2. Evaluación de riesgos y amenazas")
    print("3. Implementación de medidas de seguridad técnicas")
    print("4. Entrenamiento y concientización de los empleados")
    print("5. Auditorías y pruebas de seguridad regulares")
    print("6. Salir")

# Definir una función para manejar la selección del usuario
def handle_user_choice(choice):
    if choice in subtasks:
        # Si la opción del usuario es válida, mostrar las subtareas correspondientes
        print("Subtareas:")
        for task in subtasks[choice]:
            print(" - " + task)
    elif choice == "6":
        # Si el usuario selecciona "Salir", salir del programa
        sys.exit()
    else:
        # Si el usuario selecciona una opción inválida, mostrar un mensaje de error
        print("Opción inválida")

# Mostrar el menú
while True:
    show_menu()

    # Leer la entrada del usuario
    choice = input("Seleccione una opción: ")

    # Manejar la selección del usuario
    handle_user_choice(choice)
