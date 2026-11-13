"""
Task 3 – Validate a Student Number:
A valid student number has the form YYYY-NNNN, for example "2026-0457". Return "valid", or the
first rule that fails, checked in this order:
1. exactly 9 characters ("wrong length")
2. the character at index 4 is - ("missing '-
'")
3. the 4 characters on each side are digits ("not digits")
4. the year is between 2000 and 2026 ("year out of range")
Example 1:
Input: text = "2026-0457"
Output: valid
Example 2:
Input: text = "2O26-0457"
Output: not digits
Explanation: The second character is the letter O, not the digit zero.
Example 3:
Input: text = "1999-0001"
Output: year out of range
"""

def check_id(id):
    if len(id) != 9:
        return "wrong length"
    if id[4] != '-':
        return "missing '-' "
    
    try:
        year = int(id[0:4])
        right_digit = int(id[5:])
    except ValueError:
        return "not_digits"
    
    if not(2000 <= year <= 2026):
        return "year out of range"
    
    return "valid"


for t in ["2026-0457","2026/0457","2O26-0457","1999-0001","332"]:
    print(t, "->", check_id(t))