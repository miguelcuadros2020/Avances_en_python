numero = int(input("Ingrese el numero al cual quieres sacar el numero factorial: "))
factorial = 1
for i in range(numero,0,-1):
    factorial *= i

print(f"El numero factorial con for: {factorial}")

factorial = 1

while numero > 1:
    factorial *= numero
    numero -= 1

print(f"El factorial con while: {factorial}")