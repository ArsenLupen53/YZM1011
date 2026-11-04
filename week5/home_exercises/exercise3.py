"""
Write pyramid(n) that prints a pyramid of stars with n rows.
Row 1 has 1 star, row 2 has 3, row 3 has 5, ... (centred).
"""

def pyramid(n):
    for i in range(1, n+1):
        spaces = " " * (n-i)
        stars = "*" * (2*i-1)
        print(spaces+stars)
pyramid(3)
    