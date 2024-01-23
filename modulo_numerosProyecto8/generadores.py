def generador_perfumeria():
    for n in range(0, 1000000):
        yield f"P {1 + n}"

def generador_farmacia():
    for n in range(0, 1000000):
        yield f"F {1 + n}"

def generador_cosmetica():
    for n in range(0, 1000000):
        yield f"C {1 + n}"

p = generador_perfumeria()
f = generador_farmacia()
c = generador_cosmetica()

# Decoradores

def decoradores(servicio):
    print("\n")
    print("----------------------")
    print(f"Tu turno es:")
    if servicio == "P":
        print(next(p))
    elif servicio == "F":
        print(next(f))
    elif servicio == "C":
        print(next(c))
    print("Espere su turno")
    print("----------------------")
    print("\n")

