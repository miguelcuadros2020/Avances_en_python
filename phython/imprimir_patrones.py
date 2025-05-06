cant = int(input("Ingresa la cantidad de veces que quieres que el patron se repita: "))

print("Con for: ")

for i in range(cant,0,-1):
    print("*"*i)
    
print("Con while")

while cant>0:
    print("*" * cant)
    cant -= 1