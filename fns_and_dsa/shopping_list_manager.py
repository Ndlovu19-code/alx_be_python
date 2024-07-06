# shopping_list_manager.py

# Initialize an empty shopping list
shopping_list = []

def display_menu():
    """Display the menu options."""
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Clear list")
    print("5. Exit")

def add_item(item):
    """Add an item to the shopping list."""
    shopping_list.append(item)
    print(f"Added '{item}' to the shopping list.")

def remove_item(item):
    """Remove an item from the shopping list."""
    try:
        shopping_list.remove(item)
        print(f"Removed '{item}' from the shopping list.")
    except ValueError:
        print(f"'{item}' is not in the shopping list.")

def view_list():
    """View all items in the shopping list."""
    if shopping_list:
        print("Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("The shopping list is empty.")

def clear_list():
    """Clear all items from the shopping list."""
    shopping_list.clear()
    print("Cleared the shopping list.")

def main():
    while True:
        display_menu()
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '3':
            view_list()
        elif choice == '4':
            clear_list()
        elif choice == '5':
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the main function
if __name__ == "__main__":
    main()
