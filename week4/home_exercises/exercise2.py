"""
Select the larger discount and then apply any weekend surcharge
Base price 120TL. Under 18: 30% off; student: 15% off.
Use only the larger discount. Add 10% after discount on weekends.
"""

base_price = 120
age = 20
is_student = True
is_weekend = True

if age < 18:
    base_price = base_price * 0.7
elif is_student:
    base_price = base_price * 0.85

if is_weekend:
    base_price = base_price * 1.1

print(f"Ticket: {base_price:.2f}TL")