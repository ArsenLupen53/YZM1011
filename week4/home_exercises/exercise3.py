"""
Use Turkish vowels, Unicode letters, digits and invalid input handling.
Given input ch, classify it as vowel/other alphabetic / digit / other.
If the input length is not exactly one, print "invalid".
"""

ch = "1"
label = ""
if len(ch) != 1:
    label = "invalid"
elif ch.isdigit():  #string okuduğunu unutmayalım
    label = "digit"
elif ch in "aeıiouüöAEIİOÜUÖ":
    label = "vowel"
elif ch.isalpha():
    label = "other alphabetic"
else:
    label = "other"

print(label)