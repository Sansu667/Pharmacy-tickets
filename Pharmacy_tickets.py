import modulo_numerosProyecto8.generadores # Se importa el módulo que aloja los generadores y los decoradores

# Se crea la función "preguntar" donde el usuario ingresará la letra para el servicio que solicita
def preguntar():
    print("\n")
    print("Bienvenido/a")
    print("\n")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmética")
        try:
            print("\n")
            mi_servicio = input("Ingresa el servicio que necesitas: ").upper()
            ["P", "F", "C"].index(mi_servicio)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    modulo_numerosProyecto8.generadores.decoradores(mi_servicio)

# Se crea la función "inicio"
def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("¿Quieres sacar otro turno?: ").upper()
            ["SI", "NO"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "NO":
                print("\n")
                print("--- Gracias por utilizar nuestros servicios ---")
                break

inicio()
