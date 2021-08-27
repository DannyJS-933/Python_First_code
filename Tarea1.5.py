cookies = 99.99

cantidad = int(input("Ingrese la cantidad de galletas que desea comprar "))
descuento = 50

totalSinDescuento = cookies * cantidad
totalConDescuento = (cookies * cantidad) / descuento



seleccion = input("Desea comprar galletas del dia de hoy o las del dia enterior, ingrese la letra *o* para comprar las galletas del dia o cualquier otra tecla para continuar ")

if seleccion == "o":
    print(f"El total final es: {totalSinDescuento}\n*************************************")
else:
    print(f"Descuento aplicado por no ser galletas del dia: %{descuento}\n El total a pagar es: {totalConDescuento}\n*******************************************")








