"""
Given two sentences s1 and s2, split them into words (ignoring case) and use set operations to return
the common words, the words only in s1, the words only in s2, all words, and the words in exactly one
sentence, each as a sorted list.
"""

def compare_two_sentences(s1,s2):
    words1 = set(s1.lower().split())
    words2 = set(s2.lower().split())

    both = sorted(words1 & words2)
    only_s1 = sorted(words1 - words2)
    only_s2 = sorted(words2 - words1)
    all_s = sorted(words1 | words2)
    exactly_one = sorted(words1 ^ words2)

    return both, only_s1, only_s2, all_s, exactly_one

both, only1, only2, everything, exactly_one = compare_two_sentences("Python is fun and Python is easy","Java is hard and java is verbose")
print("Both:", both)
print("Only s1:", only1)
print("Only s2:", only2)
print("All:", everything)
print("Exactly one:", exactly_one)

