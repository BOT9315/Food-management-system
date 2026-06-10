from utils import food_items

def show_food_item():
    if not food_items:
        print("No food items in the order.")
        return
    print("\nFood items in the order:")
    for name, details in food_items.items():
        print(f"{name}: {details['quantity']} x ${details['price']} = ${details['quantity'] * details['price']}")
