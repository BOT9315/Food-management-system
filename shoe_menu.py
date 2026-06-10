from utils import menu

def show_menu():
    print("\n----- FOOD MENU -----")
    for item_id, details in menu.items():
        print(f"{item_id}. {details['name']} - ${details['price']}")
    print("----------------------")
