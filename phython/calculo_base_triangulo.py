#declaramos variables necesarias para el calculo y la captacion de datos
bases = []
alturas = []
triangulos_mayores = 0

print("\nSi no quieres ingresar mas numeros ingresa cualquier cosa que no sean numeros!!")
c = 0

#funcion para la captacion y validacion de datos.
while True:
    c += 1
    # Utilizamos el try exception para ejecutar el codigo contenido, si genera un error ejecuta la excepcion
    try:
         # pedimos los tatos al cliente y los declaramos como float
        bases.append(float(input(f"\nIngrese la base del triangulo #{c}: ")))
        alturas.append(float(input(f"\nIngrese la altura del triangulo #{c}: ")))
    
    except ValueError:
        # Print para avisar al cliente que ingreso un dato invalido
        print("\n\nIngresa un numero invalido!!\n\n")

        # if paara validar que los arrays no esten vacios y que uno no tenga mas datos que otro
        if len(bases) != 0 and len(bases) == c:

            # if para eliminar el dato adicional que tenga un array de otro
            if bases[c-1]:
                del bases[c-1]

        # if para prefuntar al usuario si quiere continuar o no des de que los arrays tengan por lo menos un dato
        if len(alturas) != 0:
            palabra = input("Desea dejar de ingresar datos? SI/NO: ").upper()
            if palabra[0] == "S":
                break
        c += -1    
c = 0  

# mostramos la lista en un estilo tabla para la estetica del mismo
print("\nnumero\tbase\taltura\tsuperficie\n")

#Asignamos los datos de cada posicion de los arrays en dos variable 
for base, altura in zip(bases,alturas):
    c += 1
    # Calculamos la superficie del triangulo
    superficie = (base*altura)/2

    # esta condicion es para los triangulos que tengan una superficie mayor a 12
    if superficie > 12:
        triangulos_mayores += 1
    
    #Mostramos los datos de cada triangulo
    print(f"#{c}\t{base}\t{altura}\t{superficie}")

#Mostramos la cantidad de triangulos que tiene una superficie mayor a 12
print(f"Numero de trianguloscon una superficie mayor a 12: {triangulos_mayores}")