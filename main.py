# Archivo: main.py
# Base del sistema de inventario (Diccionario inicial)
inventario = {
    "Resistencia 10k": 50,
    "LED Azul": 100
}

def menu():
    print("\n--- SISTEMA DE GESTIÓN DE COMPONENTES ---")
    # Próximamente se agregarán las opciones del menú aquí
    print("0. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "0":
        print("Saliendo del sistema...")
        break