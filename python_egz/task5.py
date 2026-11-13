"""
Task 5 – Digit Sum and Reversed Number:
Given a non-negative integer n, return the sum of its digits and the number written backwards. Do not
convert n to a string.
Example 1:
Input: n = 2026
Output: 10 6202
Explanation: 2 + 0 + 2 + 6 = 10, and the digits in reverse order give 6202.
Example 2:
Input: n = 90817
Output: 25 71809
Example 3:
Input: n = 0
Output: 0 0
"""

def sum_reverse(n):
    sum = 0
    remainder = 0
    reversed = ""

    while (n != 0):
        remainder = n % 10
        n = n // 10
        sum+=remainder
        reversed = reversed + f"{remainder}"

    return sum, int(reversed)

print(sum_reverse(1905))


"""
def digit_info(n):
    digit_sum = 0
    reversed_n = 0
# each iteration removes ONE digit, so n eventually reaches 0
    while n > 0:
        digit = n % 10                              # last digit: 2026 % 10 = 6
        digit_sum += digit
        reversed_n = reversed_n * 10 + digit        # shift left, then append the digit
        n //= 10                                    # drop the last digit: 2026 -> 202
    return digit_sum, reversed_n
print(digit_info(2026))
"""
