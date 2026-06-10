from utils import menu, food_items
from show_menu import show_menu
from add_food_item import add_food_item
from show_food_item import show_food_item
from total_bill import total_bill


def main():
    while True:
        print("\n-----Welcome to the Food Management System!-----")
        print("1. Show Menu of Food Items")
        print("2. Add Food Item to the Order")
        print("3. Show Order Details")
        print("4. Calculate Total Bill of the Order")
        print("5. Exit")
        choice = input("Please select an option: ")

        if choice == '1':
            show_menu()
        elif choice == '2':
            show_menu()
            while True:
                try:
                    item_id = int(input("Enter item number from menu what you want to add: "))
                    quantity = int(input("Enter quantity of the item: "))
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
                    continue
                if item_id not in menu:
                    print("Invalid menu item selected.")
                    continue
                break
            add_food_item(item_id, quantity)
        elif choice == '3':
            show_food_item()
        elif choice == '4':
            total_bill()
        elif choice == '5':
            print("Thank you for using the Food Management System. Goodbye! Have a nice day!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
