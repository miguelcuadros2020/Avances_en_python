for c in range(2,21,2):
    print(f"número par: {c}")

"""for c in range(1,16,2):
    print(f"Número impar: {c}")"""
    
cont = 0
while cont < 15:
    cont += 1
    if cont % 2 != 0:
        print(f"Número impar: {cont}")