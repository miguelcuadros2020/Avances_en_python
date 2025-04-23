print("\nBienvenido, esete es un programa para calcular el costo total de un producto!!")

#ingresos de datos

#solicitud del nombre del producto
while True:
    nombre_producto = input("\nIngrese el nombre del producto: ")
    if nombre_producto.replace(" ","").isalpha(): break
    
    print("\nEl valor ingresado no es valido, intentalo de nuevo!!, verifique que no contenga numeros ni caracteres especiales")

#solicitud y validacion del precioret
while True:
    try:
        precio_unitario = int(input("\nIngrese el valor de un solo producto: "))
        
        if precio_unitario < 0:
            raise ValueError()
        break
    
    except ValueError:
     print("\nEl valor ingresado no es valido, intentalo de nuevo!!, verifique que el dato que ingrese no contenga letras ni decimales")

#solicitud y validacion cantidad de productos adquiridos
while True:
    
    try:
        productos_adquiridos = int(input("\nIngresa la cantidad de productos adquiridos: "))
        
        if precio_unitario < 0:
            raise ValueError()
        break

    except ValueError:
        print("\nEl valor ingresado no es valido, intentalo de nuevo!!, verifique que NO sea decimal, negativo o que contenga letras")

#solicitud y validacion de descuento
while True:
    try:
        descuento = input("\nIngresa el porcentaje de descuento entre 0 y 100: ")
        
        if precio_unitario <= 0 or precio_unitario >= 100:
            raise ValueError()
        break
    except ValueError:
        print("\nEl valor ingresado no es valido, intentalo de nuevo!!, verifique que el dato ingresado este entre 0 - 100 y que NO contenga letras!!")
    
#calculo del valor neto
valNeto = int(precio_unitario) * int(productos_adquiridos)

#Muestro el valor neto y el monto final con el descuento
print(f"\nNombre del producto: {nombre_producto}\nCosto sin descuento: {valNeto}\nMonto final: {(valNeto - (valNeto * (int(descuento) / 100)))}\n")
