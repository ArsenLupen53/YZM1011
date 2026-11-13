"""
Task 1 – Even, Odd and Sign:
Given an integer n, return a string that says whether it is positive, negative or zero, and whether it is
even or odd, in the form "<n>: <sign> and <parity>".
Example 1:
Input: n = 7
Output: 7: positive and odd
Example 2:
Input: n = -4
Output: -4: negative and even
Example 3:
Input: n = 0
Output: 0: zero and even
Explanation: 0 % 2 == 0, so zero counts as even.
"""

def describe(number):
    feature = []

    if number > 0:
        feature.append("positive")
    elif number < 0:
        feature.append("negative")
    else:
        feature.append("zero")

    if number % 2 == 0:
        feature.append("even")
    else:
        feature.append("odd")

    return f"{feature[0]} and {feature[1]}"


for i in [1,5,0,-1,-2]:
    print(describe(i))
