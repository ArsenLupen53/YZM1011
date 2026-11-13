"""
Task 4 – Analyze a List of Scores:
Given a list of scores, return the average (rounded to 2 decimals), the highest score, the lowest score
and the number of passing scores (at least 70).
Example 1:
Input: scores = [72, 85, 91, 64, 85]
Output: 79.4 91 64 4
Explanation: 397 / 5 = 79.4; only 64 is below 70, so 4 scores pass.
"""

def analyze_scores(scores):
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    passing_scores = sum(1 if s >=70 else 0 for s in scores)

    return f"highest: {highest}, lowest: {lowest}, average: {average:.2f}, passing: {passing_scores}"


print(analyze_scores([72,85,91,64.3,85]))