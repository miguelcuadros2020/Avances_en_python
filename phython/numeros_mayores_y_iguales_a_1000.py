
# esta forma que es un for explicito, es mas legible y mas facil de mantener pero es un 15 -20% mas lento que el otro
# este es mas adecuado para procesos largos y complejos
"""numeros2 = []

for x in input("Ingresa los numeros separados por comas: ").split(","):
    i = int(x.strip())
    if i>=1000:
        numeros2.append(i)"""

# este es mucho mas eficiente en un 15 - 20% pero es mas dificil de mantener y de hacer una logica compleja
# es adecuado para logica y procesos pequeños
try:
    numeros =   [int(x.strip())
                for x in input("Ingresa los numeros separados por comas: ").split(",") 
                if int(x.strip()) >= 1000]

    print(f"Estos son los numeros mayores a 1000: \n\n{numeros}")
except ValueError:
    print("ingrese un numero valido, no se admiten ni letras ni decimales!!")