# class Book:
#     def __init__ (self, data):
#         self.data = data

#     def get (self, key):
#         return self.data.get(key)
    
#     def set (self, key, value):
#         self.data[key] = value
    
#     def __str__ (self):
#         print(f"{self.name} : {self.data} ")

def add():
    price = input("Add price: ")
    if price.replace(" ","").replace(".","",1).isdigit():
        price = float(price.replace(" ",""))
        quantity = input("How many you adding?: ")
        if quantity.count(".") == 0 and quantity.replace(" ","").isdigit():
            quantity = int(quantity.replace(" ",""))
            bookData = {"title": title, "price":price, "quantity":quantity}
            # book = Book(bookData)
            # bookStore.append(book)
            bookStore.append(bookData)
            print("Successfully added to inventory")
        else:
            print("Either not an integer or not a number")
    else:
        print("Invalid data")

def update():
    price = input("New pricing: ")
    if price.replace(" ","").replace(".","",1).isdigit():
        price = float(price.replace(" ",""))
        #i.set("price",price)
        i["price"]=price
        print("Successfully updated pricing")
    else:
        print("Invalid data")

bookStore = [
    {"title": "Hamlet", "price": 10.0, "quantity": 100},
    {"title": "Moby Dick", "price": 15.0, "quantity": 50},
    {"title": "The Odyssey ", "price": 20.0, "quantity": 30},
    {"title": "Necronomicon", "price": 25.0, "quantity": 10},
    {"title": "The raven", "price": 30.0, "quantity": 5}
]

while True:
    option = input("""
--- Riwi's Bookstore ---
Options: 
        1. Add a new book
        2. Search for a book in inventory
        3. Update Prices
        4. Remove books from inventory
        5. Check total pricing:
        6. Exit
""")
    match option:
        case "1":
            title = input("Add title of book you are adding: ")
            counter = 0
            for i in bookStore:
                if title.lower() == i.get("title").lower():
                    ans = input("Book already added, would you like to update update pricing instead? Y / N \n")
                    if ans.lower() == "y":
                        update()
                        break
                    elif ans.lower() == "n":
                        break
                    else:
                        print("Invalid answer")
                        break
                else:
                    counter += 1
            if counter == len(bookStore):
                add()
        case "2":
            title = input("Add title of book you are searching in inventory: ")
            counter = 0
            for i in bookStore:
                if title.lower() == i.get("title").lower():
                    print(bookStore[i])
                    break
                else:
                    counter += 1
            if counter == len(bookStore):
                print("Not on inventory or misspelled")
        case "3":
            title = input("Add title of the book you are updating it's price: ")
            counter = 0
            for i in bookStore:
                if title.lower() == i.get("title").lower():
                    update()
                    break
                else:
                    counter += 1
            if counter == len(bookStore):
                print("Not on inventory or misspelled")
        case "4":
            title = input("Add title of book you are adding: ")
            counter = 0
            for i in bookStore:
                if title.lower() == i.get("title").lower():
                    bookStore.pop(counter)
                    print("Successfully removed from inventory")
                else:
                    counter += 1
            if counter == len(bookStore):
                print("Not on inventory or misspelled")
        case "5":
            total = 0
            for i in bookStore:
                total += i.get("price") * i.get("quantity")
            print(f"Total for the inventory: {total:.2f}")
        case "6":
            break
        case _:
            print("Invalid Data")




