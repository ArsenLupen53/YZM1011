"""
Write analyze_scores(scores). Return a tuple with three values:
1. how many scores are valid (from 0 to 100)
2. how many valid scored pass (60 or more)
3. the average of the valid scores (None if there are no valid scores)
"""

def analyze_scores(scores):
    valid = [s for s in scores if 0 <= s <= 100]
    passed = sum(s >= 60 for s in valid)
    mean = sum(valid) / len(valid) if valid else None
    return len(valid),passed,mean

print(analyze_scores([72,-5,90,120,48]))
print(analyze_scores([-1,150]))
