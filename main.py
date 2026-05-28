# Archivo: main.py (Versión Final del Proyecto)
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

def descontar_componente():
    nombre = input("Nombre de pieza a descontar: ")
    if nombre in inventario:
        cantidad = int(input("Cantidad a usar: "))
        if inventario[nombre] >= cantidad:
            inventario[nombre] -= cantidad
            print(f"⚠️ Quedan {inventario[nombre]} unidades de '{nombre}'.")
        else:
            print("❌ Cantidad insuficiente en stock.")
    else:
        print("❌ Componente no encontrado.")

# NUEVA FUNCIÓN AGREGADA POR SEBASTIAN
def visualizar_inventario():
    print("--- INVENTARIO DE GAVETAS ---")
    for componente, cantidad in inventario.items():
        print(f"• {componente}: {cantidad} unidades")

def menu():
    print("--- SISTEMA DE GESTIÓN DE COMPONENTES ---")
    print("1. Registrar nuevo componente")
    print("2. Descontar componente usado")
    print("3. Visualizar Inventario")  # Opción agregada
    print("0. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_componente()
    elif opcion == "2":
        descontar_componente()
    elif opcion == "3":
        visualizar_inventario()
    elif opcion == "0":
        print("¡Gracias por usar el organizador de taller!")
        break