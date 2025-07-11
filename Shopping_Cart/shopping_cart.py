from display_functions import displayMenu, welcomeIntro

# Shopping Cart Exercise
'''
Ask user to type add, remove, show, or quit. Use a list for a cart.

Function Names:
    add_item(cart, item) - Adds an item to the cart
    remove_item(cart, item) - Removes an item if it's there
    display_cart(cart) - Prints the current shopping cart
    quit - quit condition to exit program
'''

# List to store products
products = ['apples', 'oranges', 'chicken', 'bread', 'jam', 'cheese', 'juice']

# Start with empty cart
cart = []

# Adds new items to the cart
def addItem():
    while True:
        item = input("Choose an item or (M)enu: ").lower()
        if item in ('m', 'menu', 'quit', 'q'):
            print("Returning to main menu.\n")
            break
        elif item in cart:
            print(f"You already have {item} in your cart.\n")
        elif item != cart and item in products:
            cart.append(item)
            print(f"{item.title()} has been added to your cart.\n")
            displayCart()
        elif item not in products:
            print("\nSorry, that item is not available.\n")
            print("Available products: " + ", ".join(products), "\n")
        elif item in cart:
            print(f"You already have {item} in your cart.\n")

# Removes items from the cart
def removeItem():
    item = input("Choose an item to remove: ").lower()
    if item in cart:
        cart.remove(item)
        print(f"{item.title()} have been removed from your cart.\n")
        displayCart()
    else:
        print(f"{item} was not found in your cart.\n")

# Displays current items in the cart       
def displayCart():
    if cart == []:
        print("There's nothing in the cart.\n")
    else:
        for item in cart:
            print(f"{item.title()} is in your cart.")
        print("\n")

# Intro text imported from display_functions.py
welcomeIntro()

# Loop menu that accounts for non-specified entries
while True:
    print("Sals Grocers Menu")
    displayMenu()
    makeSelection = input("\nChoose a menu option: ").lower()

    if makeSelection in ('q','quit', 'exit'):
        print("Thanks for shopping at Sals Grocers. Goodbye!")
        exit()
    elif makeSelection in ('v', 'view'):
        print("\nWe have the following products available: ")
        print(", ".join(products), "\n")
    elif makeSelection in ('a','add', 'add item', 'additem'):
        addItem()
    elif makeSelection in ('r', 'remove', 'remove item', 'removeitem'):
        removeItem()
    elif makeSelection in ('d', 'display', 'cart'):
        displayCart()
    else:
        print("That is not a valid entry.\n")
