def area_rectangulo (base, altura):
    return base * altura

def area_triangulo(base, altura):

    return (base * altura) / 2

def area_circulo(radio):
    return 3.1416 * (radio ** 2)


while True:
    print("bienvenido al programa de jared")
    print("1. calcular area de rectangulo")
    print("2. calcular area de triangulo")
    print("3. calcular area de circulo")
    print("4. salir")
    opcion_elegida = input("¿cual opcion deseas?")

    if opcion_elegida == "1": # Utilizacion de funcion para rectangulo
        mi_base = float(input("base:"))
        mi_altura = float(input("altura:"))
        area = area_rectangulo(mi_base, mi_altura)
        resultado = f"el area del rectangulo es: {area}"
        print(resultado)

    if opcion_elegida == "2":
        mi_base = float(input("base: "))
        mi_altura = float(input("altura: "))
        area = area_triangulo(mi_base, mi_altura)
        resultado = f"el area del triangulo es: {area}"
        print(resultado)

    if opcion_elegida == "3":
        mi_radio = float(input("radio: "))
        area = area_circulo(mi_radio)
        resultado = f"el area del circulo es: {area}"
        print(resultado)

    if opcion_elegida == "4":
        break
    


