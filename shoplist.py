def shopping_list():
    items = []
    print("--- SHOPPING LIST APP ---")

    n = int(input("How many items do you want to add? "))

    for i in range(n):
        it = input(f"Enter item {i+1}: ")
        items.append(it)

    print("Your shopping list:")
    print(items)

    while True:
        print("\nChoose an option:")
        print("1 Add an item")
        print("2 Update an item")
        print("3 Delete an item")
        print("4 View all items")
        print("5 Exit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Please enter a number.")
            continue

        if choice == 1:
            new_item = input("Enter the new item: ")
            items.append(new_item)
            print("Item added.")

        elif choice == 2:
            old = input("Which item do you want to update? ")
            if old in items:
                new = input("Enter the updated item: ")
                idx = items.index(old)
                items[idx] = new
                print("Item updated.")
            else:
                print("Item not found.")

        elif choice == 3:
            d = input("Which item do you want to delete? ")
            if d in items:
                items.remove(d)
                print("Item deleted.")
            else:
                print("Item not found.")

        elif choice == 4:
            print("Current items:", items)

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter between 1–5.")

shopping_list()