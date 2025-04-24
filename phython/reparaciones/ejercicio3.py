numero = int(input("Ingresa un numero: "))
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else: 
        return "impar"

resultado = es_par_o_impar(numero)
print(f"El numero {numero} es {resultado}")

