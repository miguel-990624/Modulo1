"""
README.md

This code will ask in console for the information required to add products on the inventory, the main point to work as a system to control 
and keep track of products.

We will be required to read instructions, on the menu enter a digit between 1 - 6 to perform an action.
if user types 1 - 4 we will be required to type accurately the name of the product we want. 
this will repeat until the user types the number 6 while on the menu. this will return all the requested information on screen so 
user can see and do the selected process through the terminal.
"""

"""
We create a constructor to instantiate the products that will compose my inventory
within it we can find that there are 2 functions, get to ask the program to return
the data within the specified key. And the set inner function, that will let us 
update a value within the specified key.
"""

class Product:
    def __init__ (self, data):
        self.data = data
    
    def get(self, key):
        return self.data.get(key)
    
    def set (self, key, value):
        self.data[key] = value

"""
The function setter was created, this gets the required information, and then it 
it will instantiate a new product and append it to the inventory
"""
def setter (name, quantity, price):
    productData = {"name":name, "quantity":quantity, "price":price}
    product = Product(productData)
    inventory.append(product)

"""
The add function will then ask for the required information, perform a validation
of the data that was requested and if available to be used, it will call the setter
function to instantiate and append a new product
"""
def add(name):
    quantity = input(f"How many units of {name} are available: ")
    if quantity.count(".") == 0 and quantity.replace(" ","").isdigit():
        quantity = int(quantity.replace(" ",""))
        price = input(f"Add the price for {name}: ")
        if price.replace(".","",1).replace(" ","").isdigit():
            price = float(price.replace(" ",""))
            setter (name, quantity, price)
        else:
            print("Invalid Data")
    else:
        print("Invalid Data")
"""
This function is for us to be able to change prices, we call it within a for cycle
and it will use the inner set function to update pricing acordingly
"""

def update():
    price = input("Add modified price: ")
    if price.replace(".","",1).replace(" ","").isdigit():
        price = float(price.replace(" ",""))
        i.set("price", price)
        print(f"New price updated successfully")
    else:
        print("Invalid Data")

"""
toggle function to toggle the value of a boolean value
"""

toggle = lambda x: not x

"""
We create an empty inventory array and then use the setter function
to fill the first 5 slots the test requires to have as default paramethers
"""
inventory = []

setter("Banana",10,1000)
setter("Potato",25,2500)
setter("Apple",50,1500)
setter("Carrot",30,1500)
setter("Mango",40,2000)

"""
We create the menu which is controlled by a while loop, the menu inside is
controlled by a switch or match, and depending on what the user types the code
will do one of the available options.
"""
while True:
    option = input("""
-------- Menu --------
1. Add products
2. Product search
3. Update prices
4. Remove products
5. Calculate total
6. Exit
""")
    match option:
        case "1":

            """
            first option will add a new product if the product does not exist, if it exists then
            it will ask user if they want to instead update, once it is completed, the code will
            ask if they want to add again a user, if expected value is typed then it will do another
            interaction if not back to menu
            """
            while True:
                name = input("Product name: ")
                found = False
                for i in inventory:
                    if name.lower() == i.get("name").lower():
                        found = toggle(found)
                        opt = input("Product already exist, would you like to update prices instead? Y/N\n")
                        if opt.lower() == "y":
                            update()
                            break
                        elif opt.lower() == "n":
                            break
                        else:
                            print("Invalid answer, returning to menu ...")
                            break
                if not found:
                    add(name)
                opt = input("Would you like to keep on adding products? Y/N \n")
                if opt.lower() == "y":
                    continue
                elif opt.lower() == "n":
                    print("returning to menu ...")
                    break
                else:
                    print("Invalid answer, returning to menu ...")
                    break

        case "2":
            """
            code will do a for cycle to get the name and available info on a specific product
            using the inner get functions to get the expected values.
            """
            name = input("Product name: ")
            found = False
            for i in inventory:
                if name.lower() == i.get("name").lower():
                    print("Product found ...")
                    found = toggle(found)
                    print(f"""
    for the product: {i.get("name")}, there are {i.get("quantity"):.2f} units available,
    each with a price of {i.get("price"):.2f}. 
    For a total of: {(i.get("quantity") * i.get("price")):.2f}
            """)
                    break
            if not found:
                print("Product does not exist within inventory or misspelled, try again")
        case "3":
            """
            Same update function foun before, if found in inventory it will ask customer to
            update accordingly
            """

            name = input("Product name: ")
            found = False
            for i in inventory:
                if name.lower() == i.get("name").lower():
                    print("Product found ...")
                    found = toggle(found)
                    update()
                    break
            if not found:
                print("Product does not exist within inventory or misspelled, try again")

        case "4":

            """
            This part will remove a product from the array if it exist within it, we use a 
            counter to find in which position it is on the array to know were to pop it.
            """
            name = input("Product name: ")
            counter = 0
            found = False
            for i in inventory:
                if name.lower() == i.get("name").lower():
                    print("Product found, removing from inventory ...")
                    found = toggle(found)
                    inventory.pop(counter)
                    break
                else:
                    counter += 1
            if not found:
                print("Product does not exist within inventory or misspelled, try again")

        case "5":
            """
            we will calculate the total of each product and give it individually and add it
            to the total variable then give the sumatory of everything.
            """
            print("Calculating total ...")
            total = 0
            for i in inventory:
                total += i.get("quantity") * i.get("price")
                specific = i.get("quantity") * i.get("price")
                print(f"For {i.get("name")}: {specific:.2f}")
            print(f"Total price of you inventory is: {total:.2f}")

        case "6":
            """
            We exit program.
            """
            break

        case _:
            """
            If user types anything that is not requested.
            """
            print("Invalid data, try again with one of the available options")


