def greeting_name(name:str = "World")->str:
    result = f"Hello, {name}"
    return result

def add_numbers(num1:int = 0, num2:int = 0)->int:
    result:int = num1 + num2
    return result

def area_circle(radius_circle:float = 0)->float:
    import math
    return math.pi * radius_circle ** 2

def number_even(num:int = 0):
    if num % 2 == 0:
        return True
    else:
        return False


def main():
    print("wellcome!!")
    print(greeting_name(input("Ingresa tu nombre: ")))


    print("Now we're going to add!!")
    print(add_numbers(int(input("Enter the first number: ")),int(input("Enter the second number: "))))

    print("now we're going to caldulate the area of a circle!!")
    print(area_circle(float(input("Enter the radius of the circle: "))))

    print("Now we're going to check if a number is even or not!!")
    print(f"The entered number is: {"True" if number_even(int(input("Enter the number: "))) else "False"}")

    print("Now we're going to find the greatest number!!")

main()