print("\nBienvenidos al programa del plano carteciano!!")

cantidad_puntos = {
    "Q1":0,"Q2":0,"Q3":0,"Q4":0, "centro":0
}
puntos_cuadrantes = {
    "Q1":[],"Q2":[],"Q3":[],"Q4":[],"centro":[]
}

cuadrantes_espacios = ["Q1", "Q2", "Q3", "Q4","centro"]

salida_while = True
cont = 0
while salida_while:
    try:
        salida = int(input("\nCuantos puntos (x,y) desea ingresar: "))
        saida_while = False
        
    except ValueError:
        print("\nValor invalido, Ingresalo de nuevo!! ")
        
while cont < salida + 1:
    cont += 1
    while salida_while:
        try:
            print(f"\nPunto #{salida}\n")
            puntos_x = [float(input("Ingresa X: "))]
            puntos_y = [float(input("Ingresa Y: "))]
            salida_while = False
            
        except ValueError:
            print("Valor o valores invalidos, ingresalos de nuevo")
            if len(puntos_x) == cont-1:
                del puntos_x[cont-1]
                print(puntos_x)

for x,y in zip(puntos_x,puntos_y):
    if x > 0 and y > 0:
        cantidad_puntos["Q1"] += 1
        puntos_cuadrantes["Q1"].append((x,y))
        continue
    elif x < 0 and y > 0:
        cantidad_puntos["Q2"] += 1
        puntos_cuadrantes["Q2"].append((x,y))
        continue
    elif x < 0 and y < 0:
        cantidad_puntos["Q3"] += 1
        puntos_cuadrantes["Q3"].append((x,y))
        continue
    elif x > 0 and y < 0:
        cantidad_puntos["Q4"] += 1
        puntos_cuadrantes["Q4"].append((x,y))
        continue
    else:
        cantidad_puntos["centro"] += 1
        puntos_cuadrantes["centro"].append((x,y))



ancho_puntos = max(len("cordenadas plano"),max(len(",".join([f"({x},{y})" for x,y in puntos_cuadrantes[c]]))for c in cuadrantes_espacios))


print(f"\n{'Cuadrante'}\t{'coordenadas del plano':<{ancho_puntos}}\t{'cantidad'}\n")

for unidad in cuadrantes_espacios:
    punto_str = ",".join([f"({x},{y})"for x,y in puntos_cuadrantes[unidad]])

    print(f"{unidad:<{10}}\t{punto_str:<{ancho_puntos}}\t{cantidad_puntos[unidad]}")


print("Termine")