# import sys
# import os
# import random

# # add the carpet before to PYTHONPATH or the directory
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# # and add the file from carpet before
from fun_using_week import validation_generic as fun_val

#list of products for teste
products:dict = {
    'Laptop': (1500.00, 10),
    'Smartphone': (1200.00, 20),
    'Tablet': (1800.00, 15),
    'Headphones': (2000.00, 25),
    'Smartwatch': (3000.00, 12),
    'Monitor': (4000.00, 8),
    'Keyboard': (1000.00, 30),
    'Mouse': (1200.00, 40),
    'Printer': (2500.00, 5),
    'Router': (3000.00, 18)
    }

# selection by the user
def menu():
    print("\nwhat do you need?.\n\n" \
    "1.) For add products.\n\n" \
    "2.) For consult products.\n\n" \
    "3.) For update prices the products.\n\n" \
    "4.) For remove products.\n\n" \
    "5.) For calculate value total the inventory.\n\n" \
    "6.) For extin for the program.\n")

    # validation of the input
    return fun_val(int,"Enter de option: ",[lambda x:1 <= x <= 6])

   
# Add elements to the list
def add_products(name_product:str,price_product:float,count_product:int)->None:
    products[f"{name_product.capitalize()}"] = (price_product, count_product)

# consult and print the elements
def consult_product(option:str):
    if option in products:
        print(f"{option}\tprice: {products[f"{option}"][0]:.0f} units: {products[f"{option}"][1]}")
    else:
        print("this product does not exist.")

# Update of the products
def update_product(option:str,replace:float):
    products[f"{option}"] = (replace, products[f"{option}"][1])

# delete of the products
def remove_product(option:str):
    del products[option]

#print of the products
def print_products():
    for product, data in products.items():
        print(f"Name: {product}\tPrice: {data[0]:.0f}\tUnits: {data[1]:.0f}")

# Print keys of the products
def print_keys():
    for product in products.keys():
        print(f" - {product}")

# Interaction whit the user
def main():

    # Fuctions that are used several times
    is_alpha:function = lambda x: x.replace(" ","").isalpha()
    negative:function = lambda x: 0<x
    one_leter:function = lambda x: x.strip()[0].upper()
    vali_enter_leter:function = lambda x: one_leter(x) == "S" or one_leter(x) == "N"
    list_in:function = lambda x: x in products

    print("welcome to my program!!")
    exit_cycle:bool = True # flag of the cycle

    while exit_cycle:
        option:int = menu()
        match option:

            #case for add products
            case 1:  
                    
                while exit_cycle:

                    #input and validation of products
                    name_product:str = fun_val(str,"\n\nEnter the name of the product: ",[is_alpha]).capitalize()   
                    price_product:float = fun_val(float,"\nEnter the price of the product: ",[negative])
                    count_product:int = fun_val(int,"\nEnter the cuantity: ",[negative])
                    
                    # call to the fuction for add products
                    add_products(name_product, price_product, count_product)

                    # validation of the extin
                    option:str = one_leter(fun_val(str,[is_alpha,vali_enter_leter ],"\nDo you want to enter another products? Yes/No: "))
                    if option == "N":
                        exit_cycle = False
                exit_cycle = True

                # print of elements that were added                            
                print("The products entered are: \n")
                print_products()

            #case for consult products
            case 2:
                while exit_cycle:

                    #print of the keys that exist
                    print(f"\nName of the products that exist: \n\n")
                    print_keys()

                    # Validation of the input    
                    option:str = str(input("\nEnter the name that want to consult: ")).capitalize()
                    consult_product(option) # consul of the product

                    # Validation of the extin
                    option:str = one_leter(fun_val(str,[is_alpha,vali_enter_leter ],"\nDo you want to consult another products? Yes/No: "))
                    if option == "N":
                        exit_cycle = False
                exit_cycle = True
                    
            #case for update prices of the products
            case 3:
                while exit_cycle:
                    
                    # validation of the input 
                    option:str = str(input("Enter the name of the product: ")).capitalize()
                    if list_in(option):
                        # validation of the price
                        replace_price:float = fun_val(float, "\nEnter the new price of the product: ", [negative])
                        update_product(option, replace_price)
                    else:
                        print("The price does not exist")
                    
                    # validation of the extin
                    option:str = one_leter(fun_val(str,[is_alpha,vali_enter_leter ],"\nDo you want to update another price? Yes/No: "))
                    if option == "N":
                        exit_cycle = False
                exit_cycle = True 
                
            #case for delet or remove products
            case 4:
                # validation of the input
                option:str = fun_val(str,"Enter the name that you want remove: ",[is_alpha]).capitalize()
                if list_in(option):
                    # verification of the elimination of the product
                    verification:str = one_leter(fun_val(str,[is_alpha,vali_enter_leter ], "\nYou sure? Yes/No: "))
                    if verification == "Y":
                        remove_product(option)
                else:
                    print("The product not exist")

            # case for add of the products
            case 5:
                sum_price:int = 0

                # add of the prices and the units
                for data in products.values():
                    sum_price += data[0]*data[1]
                print(f"The add of products is: {sum_price}")
            
            #case for the extin
            case 6:
                exit_cycle = False
                        

main()