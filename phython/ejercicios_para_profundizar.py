"""num1:float = 0
num2:float = 0 
num3:float = 0 
resultado:float = 0

print("Ingrese los numeros separados por enter : \n")

num1:float = input()
num2:float = input()
num3:float = input()


resultado = (num1 + num2 + num3)/3

if resultado > 7:
  print("promovido")
  pass
elif resultado <= 7 and resultado >4:
  print("regular")
  pass
else:
  print("reprobo")"""
resultado: float = 0

for i in range(0,10,1):
    num = float(input("Ingrese el numero: "))
    resultado += num

print(resultado)

