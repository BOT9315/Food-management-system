from utils import food_items

def total_bill():
    if not food_items:
        print("No food items in the order.")
        return
    grand_total = 0
    print("\nBill details:")
    for name, details in food_items.items():
        item_total = details['price'] * details['quantity']
        grand_total += item_total
        print(f"{name}: {details['quantity']} x ${details['price']} = ${item_total}")
    print(f"Total Bill: ${grand_total}")
