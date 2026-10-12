
stack = []
actual = ""

def push(item):
    stack.append(item)
    return "Página guardada..."


def isEmpty():
    return not len(stack)


def peek():
    if not isEmpty():
        return stack[-1]
    return "Sin anterior"


def pop():
    if not isEmpty():
        return stack.pop()
    return "Sin anterior"


def show():
    if isEmpty():
        return "Historial vacío..."

    message = ""
    for item in reversed(stack):
        message += f"| {item:>20} |\n"
        message += "└" + "─" * 22 + "┘\n"

    return message


def visitar(pagina):
    global actual

    if pagina == "":
        return "No puedes ingresar una página vacía"

    if actual != "":
        push(actual)

    actual = pagina
    return "Visitar: " + actual


def regresar():
    global actual

    if not isEmpty():
        actual = pop()
        return "Regresar -> " + actual

    return "Regresar -> sin anterior"


while True:
    print("\n===== HISTORIAL DE NAVEGACIÓN =====")
    print("1. Visitar página")
    print("2. Regresar")
    print("3. Mostrar página actual")
    print("4. Mostrar historial")
    print("5. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
        pagina = input("Ingrese la página web: ").strip()
        print(visitar(pagina))

    elif option == "2":
        print(regresar())

    elif option == "3":
        if actual != "":
            print("Página actual:", actual)
        else:
            print("No has visitado ninguna página")

    elif option == "4":
        print("\nHistorial de navegación:")
        print(show())
        print("Páginas guardadas:", len(stack))

    elif option == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida")
