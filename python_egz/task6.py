"""
Task 6 – Weekly Sales Table:
Given a list of lists sales, where each inner list holds one store's daily sales, use a nested loop to print
the total of each store and the number of the best store.
"""

sales = [[120,90,150],
         [80,110,95],
         [200,170,160]]

max = 0
for i in range(len(sales)):
    curr = sum(sales[i])

    if curr>max:
        max = i+1
    print(f"Store {i+1}: {curr}")

print(f"Best store: {max}")
