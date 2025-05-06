alert = lambda: print("\nValor invalido, ingresalo de nuevo.\n")

products:dict = {}
#espacios ciclos de repeticion de preguntas, mostrar que productos hay, y como queda modificado al final

def menu():
    print("\nQue desea hacer.\n\n" \
    "1.) Para añadir productos.\n\n" \
    "2.) Para consultar productos.\n\n" \
    "3.) Para actualizar precio del productos.\n\n" \
    "4.) Para eliminar productos.\n\n" \
    "5.) Para calcular valor total del inventario.\n\n" \
    "6.) Para salir del programa\n")
    exit_cycle:bool = True

    while exit_cycle:
        try:
            option  = int(input("Enter de option: "))
            if not(1<=option<=6):
                raise ValueError()
            
            exit_cycle = False
            return option
        except ValueError:
            alert()

def add_products(name_product,price_product,count_product)->None:
    products[f"{name_product.capitalize()}"] = (price_product, count_product)

def consult_product(option):
    if option in products:
        print(f"{option}\tprecio: {products[f"{option}"][0]:.0f} cantidad: {products[f"{option}"][1]}")
    else:
        print("Ese producto no existe.")

def update_product(option,replace):
    products[f"{option}"] = (replace, products[f"{option}"][1])

def remove_product(option):
    del products[option]

calculate_add_products = lambda x,y: x*y
def main():
    print("welcome to my program!!")
    exit_cycle:bool = True

    while exit_cycle:
        option = menu()
        match option:
            case 1:
                exit_cycle:bool = True
                while exit_cycle:
                    try:
                        name_product = str(input("\n\nIngrese el nombre del nuevo producto: "))
                        if len(name_product) == 0:raise ValueError()

                        price_product = float(input("\nIngrese el precio del producto: "))
                        if 0 > price_product: raise ValueError()

                        count_product = int(input("\nIngrerse la cantidad de productos que hay: "))
                        if 0 > count_product: raise ValueError()

                        add_products(name_product, price_product, count_product)

                        if input("\nDesea ingresar otro producto? SI/NO: ").upper()[0] == "N":
                            exit_cycle = False
                        
                    except ValueError:
                        alert()
                exit_cycle = True
                print("Los productos ingresados son: \n")
                for product, data in products.items():
                    print(f"nombre: {product}\tprecio: {data[0]:.0f}\tcantidad: {data[1]:.0f}")

            case 2:
                print(f"\nLos productos que hay son los siguientes: \n\n")
                for product in products.keys():
                    print(f" - {product}")
                    
                option = str(input("\nIngresa el nombre del producto que quieres consultar (en la parte superior estan las opciones): ")).capitalize()
                consult_product(option)
                    
            
            case 3:
                option = str(input("Enter the name of a product: ")).capitalize()
                if option in products:
                    while exit_cycle:
                        try:
                            replace_price = float(input("Enter the cost of product: "))
                            update_product(option,replace_price)
                            exit_cycle = False
                        except ValueError:
                            alert()
                    exit_cycle = True
                else:
                    print("the product not exist.")
            
            case 4:
                option = str(input("Enter the name that want remove ")).capitalize()
                if option in products:
                    remove_product(option)
                else:
                    print("The product not exist")

            case 5:
                sum_price = 0
                for data in products.values():
                    sum_price += calculate_add_products(data[0], data[1])
                print(f"the add of products is: {sum_price}")
            
            case 6:
                exit_cycle = False
                        

main()