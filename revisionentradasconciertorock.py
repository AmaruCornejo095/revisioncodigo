stock_concepcion = 500
stock_puente_alto = 1300
stock_muelle_baron = 100
stock_muelle_vergara = 50
entradas_fortificados = []

def menu():
    print("\n=====Totem Autoservicio Conciertos Rock And Chile In Chile====")
    print("1. Comprar entrada en concepcion.")
    print("2. Comprar entrada en puente alto.")
    print("3. Comprar entrada en muelle barón, Valparaiso.")
    print("4. Comprar entrada en muelle vergara, Viña del mar.")
    print("5. Salir.")

def validar_codigo_fortificados(codigo):
    if len(codigo) < 6:
        return False
    if " " in codigo:
        return False
    tiene_mayuscula = False
    for caracter in codigo:
        if caracter.isupper():
            tiene_mayuscula = True
            break
    if not tiene_mayuscula:
        return False
    
    tiene_numero = False
    for caracter in codigo:
        if caracter.isdigit():
            tiene_numero = True
            break
    if not tiene_numero:
        return False       
    return True     

def nombre_repetido(nombre, lista_entradas):
    for e in lista_entradas:
        if e["nombre"].lower() == nombre.lower():
            return True
    return False

def entradas_disp():
    return stock_concepcion + stock_puente_alto + stock_muelle_baron + stock_muelle_vergara - len(entradas_fortificados)

def comprar_concepcion():
    global stock_concepcion
    if stock_concepcion == 0:
        print("No quedan entradas disponibles.")
        return

    print("\n-- Compra en Concepción --")  #revision
    nombre = input("Ingrese el nombre de comprador: ").strip()  #revision
    if nombre_repetido(nombre, entradas_fortificados):
        print("Error, el nombre ya está registrado.")
        return

    while True:
        codigo = input("Ingrese código de confirmacion: ").strip()
        if validar_codigo_fortificados(codigo):
            print("Código validado.")  #revision
            break
        else:
            print("Error: código de confirmación inválido.")  #revision

    entradas_fortificados.append({"nombre": nombre, "codigo": codigo})
    stock_concepcion -= 1
    print(f"Entrada registrada! Stock restante: {stock_concepcion}")

def comprar_puente_alto():
    global stock_puente_alto
    if stock_puente_alto == 0:
        print("No quedan entradas disponibles.")
        return

    print("\n-- Compra en Puente Alto --")  #revision
    nombre = input("Ingrese el nombre de comprador: ").strip()  #revision
    if nombre_repetido(nombre, entradas_fortificados):
        print("Error, el nombre ya está registrado.")
        return

    try:
        cantidad = int(input("Cantidad de entradas (máx 3): "))  #revision
    except ValueError:
        print("Error: debe ingresar un número válido.")  # ✅ NUEVO
        return

    if cantidad < 1 or cantidad > 3:  #revision 
        print("Error: solo se permiten entre 1 y 3 entradas por persona.")
        return

    if cantidad > stock_puente_alto:  #revision
        print("Error: no hay suficiente stock disponible.")
        return

    entradas_fortificados.append({"nombre": nombre, "cantidad": cantidad})  #revision
    stock_puente_alto -= cantidad
    print(f"Entradas registradas! Stock restante: {stock_puente_alto}")

def comprar_muelle_baron():
    global stock_muelle_baron
    if stock_muelle_baron == 0:
        print("No quedan entradas disponibles.")
        return

    print("\n-- Compra en Muelle Barón, Valparaíso --")  #revision
    nombre = input("Ingrese el nombre de comprador: ").strip()
    if nombre_repetido(nombre, entradas_fortificados):
        print("Error, el nombre ya está registrado.")
        return

    entradas_fortificados.append({"nombre": nombre, "tipo": "G"})  #revision
    stock_muelle_baron -= 1
    print("Tipo de entrada asignado: G")  #revision
    print(f"Entrada registrada! Stock restante: {stock_muelle_baron}")

def comprar_muelle_vergara():
    global stock_muelle_vergara
    if stock_muelle_vergara == 0:
        print("No quedan entradas disponibles.")
        return

    print("\n-- Compra en Muelle Vergara, Viña del Mar --")  #revision
    nombre = input("Ingrese el nombre de comprador: ").strip()
    if nombre_repetido(nombre, entradas_fortificados):
        print("Error, el nombre ya está registrado.")
        return

    tipo = input("Tipo de entrada (Sun=Sunset, Ni=Night): ").strip().lower()  #revision
    if tipo not in ["sun", "ni"]:  #revision
        print("Error: tipo de entrada inválido.")
        return

    entradas_fortificados.append({"nombre": nombre, "tipo": tipo})  #revision
    stock_muelle_vergara -= 1
    print(f"Entrada registrada! Stock restante: {stock_muelle_vergara}")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()  #revision
        if opcion == "1":
            comprar_concepcion()
        elif opcion == "2":
            comprar_puente_alto()
        elif opcion == "3":
            comprar_muelle_baron()
        elif opcion == "4":
            comprar_muelle_vergara()
        elif opcion == "5":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")  #revision

if __name__ == "__main__":
    main()
