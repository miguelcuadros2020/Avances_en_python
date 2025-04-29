print("\nbienvenido al programa de calificaciones!!\n")






#No cree funciones para cosas reperirivas porque el profesor no me lo permitio
#No consulte como podria hacerlo mas eficiente ni mas corto por que me dijeron que lo hiciera simple
#se que hay varia cosas que puedo hacer mas eficinte y menos redundante pero no quiero hacer algo que me guste para saber que no era lo que me pidiero y me pongan mala nota (experiancias)







#creamos la fucion para separa un texto con comas 
nums = []
variable = ""
promedio = 0
while True:
    try:
        for x in input("Ingresa las notas separadas por comas: ") + ",":
            
            #usamos un if para concatenar y añadir a la lista
            if x == ",":
                nums.append(variable)
                variable = ""
            else:
                variable += x

        #creamos una fincion para verificar que los numeros ingresados esten entre 0 y 100, de lo contrarise reinicia
        for i in nums:
            x = int(i)
            if not (x <= 100 and x >= 0):
                raise ValueError()

        break
    except ValueError:

        print("Numeros invalidos, verifique que ho halla ingresado ni letras ni caracteres diferentes de comas o espacios!!\n verifique que las notas estan en el rango de 0 a 100!!")
        nums.clear()

#Preguntamos si el usuario quiere o no hacer la consulta
while True:
    solicitud = input("Desea saber si el estudiante aprovo o reprobo? SI/NO: ").upper()
    if solicitud[0] == "S" or solicitud[0] == "N":
        break
    print("valor invalido, ingreselo nuevamente!!")

# creamos una funcion para saber si aprobo o reprobo segun el promedio y la nota ingresada por el profesor
while solicitud[0] == "S":
    try:
        #pedimos datos y validamos
        nota_minima = float(input("Ingresa la nota minima que debe tener el estudiante a en promedio para aprobar la materia: "))
        if not(nota_minima <= 0 and nota_minima >=100): raise ValueError()

        #sacamos promedio
        promedio = sum(nums)/len(nums)

        # definimos si el estudiante aprueba o reprueba
        if sum(nums) < nota_minima:
            print("el estudiante fue reprobado!!")
        else:
            print("el estudiante fue aprobado!!")
        break
    except ValueError:
        print("Valor invalido, intentalo de nuevo!!")    

#preguntamos si el usuario quiere o no hacer la consulta
while True:
    solicitud = input("Desea saber que notas son superiores a las que solicite? SI/NO: ").upper()
    if solicitud[0] == "S" or solicitud[0] == "N":
        break
    print("valor invalido, ingreselo nuevamente!!")

# creamos una funcion para que el usuario pueda consultar que notas son iguales o mayore a la consultada
while solicitud[0] == "S":
    try:
        #solicitamos y validamos los datos
        nota_consulta = float(input("Ingresa la nota que quieres consultar para mostrar las notas mayores a esa: "))
        if not(nota_consulta <=0 and nota_consulta >= 100): 
            raise ValueError()

        #Imprimimos las notas mayores a la consultada
        print(f"Notas mayores a: {nota_consulta}")
        for x in nums:
            if x > nota_consulta:
                print(x)

        break
    except ValueError:
        print("Valor invalido, intentelo de nuevo")

#preguntamos si el usuario quiere o no hacer la consulta
while True:
    solicitud = input("Desea consultar cuantas notas de las mismas hay segun el valor ingresado? SI/NO: ").upper()
    if solicitud[0] == "S" or solicitud[0] == "N":
        break
    print("valor invalido, ingreselo nuevamente!!")

# Funcion para consultar una nota en especifico
while solicitud[0] == "S":
    try:
        #solicitamos datos y validamos
        nota_igual = float(input("Ingresa la nota en espacifico que quieres consultar: "))
        if not(nota_igual <=0 and nota_igual >= 100): 
            raise ValueError()
        
        #Imprimimos las notas que sean iguales a la solicitada
        print(f"Las notas iguales a: {nota_igual} son: ")
        for x in nums:
            if x == nota_igual:
                print(x)

        break
    except ValueError:
        print("Valor invalido, intentalo de nuevo!!")
