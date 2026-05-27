# === ITERACIÓN 1: CÓDIGO BASE DEL SISTEMA ===

# Estructura de datos global para almacenar los libros
libros_biblioteca = {
    "101": {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "disponible": True},
    "102": {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": True}
}

def registrar_libro():
    print(" REGISTRAR NUEVO LIBRO ")
    codigo = input("Ingrese el código único del libro (ISBN/ID): ")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    
    libros_biblioteca[codigo] = {"titulo": titulo, "autor": autor, "disponible": True}
    print(f"¡Libro '{titulo}' registrado exitosamente en el catálogo!")

def menu_biblioteca():
    while True:
        print("SISTEMA DE BIBLIOTECA UNIMAR ")
        print("1. Registrar Nuevo Libro")
        print("3. Salir del Sistema")  # Se deja el espacio para las opciones de la iteración 2
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_libro()
        elif opcion == "3":
            print("Cerrando sesión en la biblioteca...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if _name_ == "_main_":
    menu_biblioteca()