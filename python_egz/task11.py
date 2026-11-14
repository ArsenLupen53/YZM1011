def sell(inventory, item, quantity):
    if quantity <= 0:
        return "Quantity must be positive"
    if item not in inventory:
        return "Unknown item"
    if inventory[item] < quantity:
        return "Insufficient stock"

    inventory[item] -= quantity
    return "Sale completed"

inventory = {"pen":5,"notebook":2}
print(sell(inventory,"pen",3))
print(sell(inventory,"notebook",4))
print(sell(inventory,"eraser",1))
print("Remaining inventory:",inventory)