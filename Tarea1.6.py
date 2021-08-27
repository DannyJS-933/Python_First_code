teclado = 200
mouse = 75

print("Que desea comprar?")

seleccion = input("Presiones la telca *m* para mouse o presiones la tecla *t* para teclado: ")

if seleccion == "m":
    cantidad = int(input("Ingrese la cantidad de mouses que desea comprar: "))
    pesoTotal = cantidad * mouse
    print(f"El peso total es: {pesoTotal}")
elif seleccion == "t":
    cantidad1 = int(input("Ingrese la cantidad de teclados que desea comprar: "))
    pesoTotal1 = cantidad1 * teclado
    print(f"El peso total es: {pesoTotal1}")
else:
    print("No selecciono ninguna opcion")