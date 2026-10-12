
stack = []



def push(item, capacity):
    if item == "":
        return "El código no puede estar vacío"

    if item in stack:
        return "Esa caja ya existe"

    if not is_full(capacity):
        stack.append(item)
        return "Caja apilada correctamente..."

    return "Pila llena"


def isEmpty():
    return not len(stack)


def is_full(capacity):
    return len(stack) == capacity


def peek():
    if not isEmpty():
        return stack[-1]
    return "Pila vacía..."


def pop():
    if not isEmpty():
        return stack.pop()
    return "Pila vacía..."


def show():
    if isEmpty():
        return "Pila vacía..."

    message = ""
    for item in reversed(stack):
        message += f"| {item:>6} |\n"
        message += "└" + "─" * 8 + "┘\n"

    return message


capacity = 5

while True:
    print("\n===== CONTROL DE BODEGA =====")
    print("1. Apilar caja")
    print("2. Desapilar caja")
    print("3. Consultar tope")
    print("4. Mostrar pila")
    print("5. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
        item = input("Ingrese el código de la caja: ").strip()
        print(push(item, capacity))

    elif option == "2":
        print("Caja retirada:", pop())

    elif option == "3":
        print("Caja en el tope:", peek())

    elif option == "4":
        print("\nCajas almacenadas:")
        print(show())
        print("Cantidad de cajas:", len(stack))

    elif option == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida")
