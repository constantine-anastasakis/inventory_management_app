

import csv
import os

def menu(username="default_user", products_count=100):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!

    There are {products_count} products in the database.

    Please select one of the following options:

        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about any product in the database.
        'Create'  | Add a new product to the database.
        'Update'  | Edit a product in the database.
        'Destroy' | Delete a product from the database.
        'Reset'   | Reset the product list.
        'Quit'    | End the program.

    """ # end of multi- line string. also using string interpolation

    return menu

def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename) #reading some file (__file__) means the directory where the file belongs
    print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = []

    #TODO: open the file and populate the products list with product dictionaries

    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) # special function Dictionary Reader
        for row in reader: #loop through the rows
            #print('36 row:', row)
            products.append (dict(row))
    return products

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
    #TODO: open the file and write a list of dictionaries. each dict should represent a product.

    with open(filepath, "w") as csv_file: #"w" means opening it for writing
        writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
        writer.writeheader() # uses fieldnames set above to write a dictionary

        for p in products:
            writer.writerow(p)


def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    print (products)
    write_products_to_file(filename, products)

def run():
    # First, read products from file...


    oper_name = input ("Please enter username: ")
    while True:
        # Then, prompt the user to select an operation...
        products = read_products_from_file()
        products_count = len(products)
        print(menu(username = oper_name, products_count = products_count)) #TODO instead of printing, capture user input

        command = input ("Please select an operation: ")
        if command == "List":
            print ("""
    ---------------------------
    LISTING ALL PRODUCTS:
    ---------------------------""")
            for product_dict in products:
                the_id = product_dict['id']
                the_name = product_dict['name']
                the_price = product_dict['price']
                #print(the_id, the_name, the_price)
                print("%s, %s, $%.2f" % (the_id, the_name, float(the_price)))
        elif command == "Show":
            print()
            product_id = input ("Please enter a product identifier: ")
            print ("""
    ---------------------------
    SHOWING A PRODUCT:
    ---------------------------""")
            for product_dict in products:
                the_id = product_dict['id']
                if the_id == product_id:
                    print (product_dict)
                    break
            else:
                print('Sorry', product_id, 'not found')
        elif command == "Quit" or command == "q":
            break # out of the while loop
        elif command == "Create":
            print()
            new_product_name = input ("Ok, please provide the new product's name: ")
            new_product_aisle = input ("Ok, please provide the new product's aisle: ")
            new_product_department = input ("Ok, please provide the new product's department: ")
            new_product_price = input ("Ok, please provide the new product's price: ")
            print ("""
    ---------------------------
    CREATING A NEW PRODUCT:
    ---------------------------""")
            product_dict = products[-1]
            the_id = product_dict['id']
            id_num = int(the_id)
            new_product_id = str(id_num + 1)
            new_product_dict = {}
            new_product_dict['id'] = new_product_id
            new_product_dict['name'] = new_product_name
            new_product_dict['aisle'] = new_product_aisle
            new_product_dict['department'] = new_product_department
            new_product_dict['price'] = new_product_price
            products.append(new_product_dict)
            print(new_product_dict)

        elif command == "Update":
            print()
            update_product_id = input("Ok, please specify the product's identifier: ")
            for product_dict in products:
                this_id = product_dict['id']
                if this_id == update_product_id:
                    # do the updated
                    updated_product_name = input ("Ok, please provide the product's updated name: ")
                    updated_product_aisle = input ("Ok, please provide the product's updated aisle: ")
                    updated_product_department = input ("Ok, please provide the product's updated department: ")
                    updated_product_price = input ("Ok, please provide the product's updated price: ")
                    product_dict['name'] = updated_product_name
                    product_dict['aisle'] = updated_product_aisle
                    product_dict['department'] = updated_product_department
                    product_dict['price'] = updated_product_price

                    print ("""
    ---------------------------
    UPDATING A PRODUCT:
    --------------------------- """)

                    print(product_dict)
                    break
                else:
                    print('Sorry', update_product_id, 'not found')
                    break

        elif command == "Destroy":
            print()
            destroy_product_id = input("Ok, please specify the product identifier: ")
            for product_dict in products:
                destroy_id = product_dict['id']
                if destroy_id == destroy_product_id:
                    print ("""
    ---------------------------
    DELETING A PRODUCT:
    ---------------------------""")
                    print(destroy_product_id)
                    products.remove(product_dict)
                    break
            else:
                print('Sorry', destroy_product_id, 'not found')
                break

        elif command == "Reset":
            print()
            reset_products_file(filename="products.csv", from_filename="products_default.csv")
            print ("""
    ---------------------------
    RESETTING PRODUCT LIST:
    ---------------------------""")


    write_products_to_file(products=products)


if __name__ == "__main__":
    run()
