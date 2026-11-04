"""
Write merge_enrollments(a,b). a and b are the student lists of course A and course B (a name may repeat). Return three sorted lists:
1. students in both courses
2. students only in course A
3. studnets in at least one course
Hint: turn each list into a set first.
"""

def merge_enrollments(a,b):
    left = set(a)
    right = set(b)
    both = sorted(left & right)
    only_a = sorted(left - right)
    either = sorted(left | right)
    return both, only_a, either

a = ["Ada", "Mert", "Ada", "Ece"]
b = ["Ece", "Ali"]
print(merge_enrollments(a,b))
print(merge_enrollments(["Can"],["Can","Ece"]))