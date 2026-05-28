inventario = {
    "Resistencia 10k": 50,
    "LED Azul": 100
}

def registrar_componente():
    nombre = input("Nombre de pieza: ")
    cantidad = int(input("Cantidad: "))
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        inventario[nombre] = cantidad
    print(f"✅ {cantidad} unidades de '{nombre}' añadidas.")

def menu():
    print("\n--- SISTEMA DE GESTIÓN DE COMPONENTES ---")
    print("1. Registrar nuevo componente")  # <-- LÍNEA 15 DE GABRIEL
    print("0. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_componente()
    elif opcion == "0":
        break 