#Imprimimos el hola mundo
"""print("¡Hola mundo!!")"""

#Ejercicio para hacer un calculo aritmetico
"""print(((3+2)/(2*5))**2)"""

#calculo del pago segun las horas trabajadas
"""horasTrab = float(input("Ingrede la cantidad de horas trabajadas: "))
costo = float(input("Ingrese el coste de las horas: "))

print(f"tu pago es de {(horasTrab * costo):.0f}")"""

#suma desde el 1 hasta n
"""numero = int(input("Ingresa el numero al cual le quieras hacer el calculo: "))
print(f"La sumatoria desde el numero 1 hasta el {numero} es de: {((numero * (numero + 1))/2):.0f}")"""

#Calculo del imc de masa corpral adecuada para su curpo
"""masa = float(input("Ingrese su peso en kilogramos: "))
estatura = float(input("Introduce tu estatura en metros: "))

print(f"Tu indice de masa corporal es {(masa/(estatura**2)):.2f}")"""

#Ejercicio para una divicion """if x.isdigit() else None""" 
"""nums = [int(round(float(x))) for x in [input("ingresa dos numeros: "), input()]]
nums.append(int(input("Ingresa dos numeros")))
nums.append(int(input()))

print(f"{nums[0]} entre {nums[1]} da un cosiente {nums[0]/nums[1]} y un resto {nums[0]%nums[1]}")"""



#Calculo de inverciones a largo palzo
"""print("vienvenido a programa del calculo de rendimeinro a invercion a largo plazo!!!")
invercion = float(input("Ingresa la cantidad que quieres invertir: "))
interes = float(input("Ingresa el interes anual: "))
anos = float(input("Ingresa el numero de años que deseas invertir: "))

valfin = invercion*(1+interes)**anos

print(f"El capital al final del periodo es de: {valfin:.2f}")"""

#10 jugueteria que tiene exito en dos productos, muñecas y payasos
"""munecas = int(input("Ingresa la cantida de muñecas vendidos: "))
payasos = int(input("ingresa la cantidad de payasos vendidos: "))

peso = (payasos * 112) + (munecas * 75)

print(f"El peso del paquete es de: {peso}")"""



# 11 calcular la tasa de interes de una cuenta de ahorros al 4%

print("Bienvenido a la calculadora de interes compuesto al 4%")
capital = int(input("Ingresa el capital que quieres invertir: "))
tiempo = int(input("Años de la inverción: "))

for i in range(0,1+tiempo):
    captotal = capital*(1+0.04)**i
    print(f"En el año {i} el interes acomulado es de: {(captotal-capital):.2f} con un total acomulaso enese año de: {(captotal):.2f}")
