# TechFuture Analyzer
# Proyecto Integrador

def mostrar_menu():
    print("=== TechFuture Analyzer ===")
    print("1. Analizar ventas")
    print("2. Analizar clientes")
    print("3. Salir")

def analizar_ventas():
    ventas = [1200, 1500, 1800, 2000]
    total = sum(ventas)
    promedio = total / len(ventas)
    print("Total de ventas:", total)
    print("Promedio de ventas:", promedio)

def analizar_clientes():
    clientes = ["Juan", "Maria", "Carlos", "Ana"]
    print("Lista de clientes registrados:")
    for cliente in clientes:
        print("-", cliente)

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        analizar_ventas()
    elif opcion == "2":
        analizar_clientes()
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")
