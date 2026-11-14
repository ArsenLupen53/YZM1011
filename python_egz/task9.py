"""
Task 9 – Shopping Cart Bill:
Given a dictionary prices and a list of (item, quantity) tuples cart, print the cost of each item
and the total. Print "<item>: not found" for an item that has no price.
"""

prices = {"apple":5,"bread":12,"milk":25}
cart = [("apple",4),("milk",1),("cheese",2)]

total = 0

for item,quantity in cart:
    if item in prices:
        cost = prices[item] * quantity
        print(f"{item}: {cost}")
        total += cost
    else:
            print(f"{item}: not found")

print("Total:",total)