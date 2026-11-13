"""
Task 2  Parking Fee:
Given the parked minutes, return the parking fee. The first 60 minutes are free, then every started hour
costs 15 TL, and the fee is at most 120 TL. Return "invalid" for a negative input.
Hint: the number of started hours is (minutes minutes gives 2.
+ 59) // 60. For example, 60 minutes gives 1 and 61
Example 1:
Input: minutes = 45
Output: 0
Explanation: Inside the free first hour.
Example 2:
Input: minutes = 150
Output: 30
Explanation: 150 minutes start 3 hours; the first is free, so 2 × 15 = 30.
Example 3:
Input: minutes = 600
Output: 120
Explanation: 10 started hours give 9 × 15 = 135, which is capped at 120.
"""

def park_fee(minutes):
    if minutes < 0:
        return "invalid"
    else:
        hours = (minutes + 59) // 60
        fee = 15 * hours - 15
        if (fee > 120):
            return 120
        else:
            return fee
        
for m in [45, 61, 150, 600,-5]:
    print(m, "->",park_fee(m))


