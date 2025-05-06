deposito = 100000
salida_while = True
while salida_while :
    print(f"su deposito es de {deposito}")
    
    solicitud = str(input("Desea ingresar dinero a su deposito? SI/NO: ").upper())
    
    if solicitud[0] =="S":
        cantidad_ingresar = int(input("Ingresa la cantidad que quieres ingresar: "))
        deposito += cantidad_ingresar
        print(f"su deposito es de {deposito}")
    
    solicitud = str(input("Desea retirar dinero? SI/NO: ").upper())
    if solicitud[0] == "S":
        cantidad_retirar = int(input("Ingresa la cantidad que quieres retirar: "))
        if cantidad_retirar < deposito:
            deposito -= cantidad_retirar
            print(f"su deposito es de {deposito}")
        else:
            print("La cantidad que deseas retirar es mayor a la que tienes en el deposito!!")
    
    solicitud = str(input("Desea salir de la operacion? SI/NO: ").upper())
    if solicitud[0] == "S":
        salida_while = False