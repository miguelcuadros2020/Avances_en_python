print("1. Suma")
print("2. Resta")
opcion = input("Elige una opción (1/2): ")

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

if opcion == "1" :
    print(f"Resultado: {num1 + num2}")
elif opcion == "2":
        print(f"Resultado: {num1 - num2}")
else:
        print("Opción inválida.")