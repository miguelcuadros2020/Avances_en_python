print("\nbienvenido al programa de calificaciones!!\n")






#No cree funciones para cosas reperirivas porque el profesor no me lo permitio
#No consulte como podria hacerlo mas eficiente ni mas corto por que me dijeron que lo hiciera simple
#se que hay varia cosas que puedo hacer mas eficinte y menos redundante pero no quiero hacer algo que me guste para saber que no era lo que me pidiero y me pongan mala nota (experiancias)







#creamos la fucion para separa un texto con comas 
nums = []

while True:
    try:
        variable = ""
        for x in input("\nIngresa las notas separadas por comas: ") + ",":
            
            #usamos un if para concatenar y añadir a la lista
            if x == ",":
                nums.append(float(variable))
                variable = ""
            else:
                variable += x

        #creamos una fincion para verificar que los numeros ingresados esten entre 0 y 100, de lo contrarise reinicia
        for x in nums:
            if not (x <= 100 and x >= 0):
                raise ValueError()

        break
    except ValueError:

        print("\nNumeros invalidos, verifique que ho halla ingresado ni letras ni caracteres diferentes de comas o espacios!!\n verifique que las notas estan en el rango de 0 a 100!!")
        nums.clear()
 
#Preguntamos si el usuario quiere o no hacer la consulta
while True:
    try:
        solicitud = input("\nDesea saber si el estudiante aprovo o reprobo? SI/NO: ").upper()
        if solicitud[0] != "S" and solicitud[0] != "N":
            raise ValueError()
        
        break
    except ValueError:
        print("\nvalor invalido, ingreselo nuevamente!!")
# creamos una funcion para saber si aprobo o reprobo segun el promedio y la nota ingresada por el profesor
while solicitud[0] == "S":
    try:
        #pedimos datos y validamos
        nota_minima = float(input("\nIngresa la nota minima que debe tener el estudiante a en promedio para aprobar la materia: "))
        if not(0 <= nota_minima <= 100):
            raise ValueError()

        # definimos si el estudiante aprueba o reprueba
        if sum(nums) < nota_minima:
            print("\nel estudiante fue reprobado!!")
        else:
            print("\nel estudiante fue aprobado!!")
        
        #imprimimos el promedio
        print(f"El promedio es de: {sum(nums)/len(nums)}")
        
        break
    except ValueError:
        print("\nValor invalido, intentalo de nuevo!!")    

#preguntamos si el usuario quiere o no hacer la consulta
while True:
    try:
        solicitud = input("\nDesea saber que notas son superiores a las que solicite? SI/NO: ").upper()
        if solicitud[0] != "S" and solicitud[0] != "N":
            raise ValueError()
        
        break
    except ValueError:
        print("\nvalor invalido, ingreselo nuevamente!!")

# creamos una funcion para que el usuario pueda consultar que notas son iguales o mayore a la consultada
while solicitud[0] == "S":
    try:
        #solicitamos y validamos los datos
        nota_consulta = float(input("\nIngresa la nota que quieres consultar para mostrar las notas mayores a esa: "))
        if not(0 <= nota_consulta <= 100): 
            raise ValueError()

        #Imprimimos las notas mayores a la consultada
        print(f"\nNotas mayores a: {nota_consulta}")
        for x in nums:
            if x > nota_consulta:
                print(x)

        break
    except ValueError:
        print("\nValor invalido, intentelo de nuevo")

#preguntamos si el usuario quiere o no hacer la consulta
while True:
    try:
        solicitud = input("\nDesea consultar cuantas notas de las mismas hay segun el valor ingresado? SI/NO: ").upper()
        if solicitud[0] != "S" and solicitud[0] != "N":
            raise ValueError()
        
        break
    except ValueError:
        print("\nvalor invalido, ingreselo nuevamente!!")

# Funcion para consultar una nota en especifico
while solicitud[0] == "S":
    try:
        #solicitamos datos y validamos
        nota_igual = float(input("\nIngresa la nota en espacifica que quieres consultar: "))
        if not(0 <= nota_igual <= 100): 
            raise ValueError()
        
        #Imprimimos las notas que sean iguales a la solicitada
        print(f"\nLas notas iguales a: {nota_igual} son: ")
        for x in nums:
            if x == nota_igual:
                print(x)

        break
    except ValueError:
        print("\nValor invalido, intentalo de nuevo!!")
