from utils import menu, food_items

def add_food_item(item_id, quantity):
    if item_id not in menu:
        print("Invalid menu item selected please choose a valid item.")
        return

    name = menu[item_id]['name']
    price = menu[item_id]['price']

    if name in food_items:
        food_items[name]['quantity'] += quantity
    else:
        food_items[name] = {'price': price, 'quantity': quantity}

    print(f"{quantity} {name}(s) added to the order.")
