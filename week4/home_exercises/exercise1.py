"""
Parse customer name, quantity, unit price from a | -separated record.
Add 20% VAT(Value Added Tax); reject nonpositive quantitiy or price
"""

record = "  Ada | 3 | 19.90  "
record = record.strip()

record = record.split(" | ")
customer = record[0]
quantity = int(record[1])
price = float(record[2]) * 1.2


"""
Different solution
record = "  Ada | 3 | 19.90  "
parts = record.split("|")
name = parts[0].strip()
qty = int(parts[1].strip())
price = float(parts[2].strip())
"""

if quantity < 0 or price < 0:
    print("Invalid quantity or price")
else:
    print(f"Customer: {customer}")
    print(f"Total incl. VAT: {price * quantity}")
    