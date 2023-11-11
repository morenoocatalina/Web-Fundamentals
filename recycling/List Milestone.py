cart = []

print("Welcome to the Shopping Cart Program!")

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    choice = int(input("Please enter an action: "))

    if choice == 1:
        item_to_add = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item_to_add}'? "))
        cart.append((item_to_add, price))
        print(f"'{item_to_add}' has been added to the cart.")
    if choice == 2:
        print("The contents of the shopping cart are:")
        for i, (item, price) in enumerate(cart, start=1):
            print(f"{i}. {item} - ${price:.2f}")
    if choice == 3:
        index_to_remove = int(input("Which item would you like to remove? "))
        if 1 <= index_to_remove <= len(cart):
            removed_item = cart.pop(index_to_remove - 1)
            print(f"{removed_item[0]} has been removed.")
        else:
            print("Invalid index. No item removed.")
    if choice == 4:
        total_price = sum(price for _, price in cart)
        print(f"The total price of the items in the shopping cart is ${total_price:.2f}")
    if choice == 5:
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
