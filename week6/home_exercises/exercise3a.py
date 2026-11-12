"""
Make two charts and save each one as a PNG file:
1. counts.png: a bar chart of how many A and B labels there are
Give both charts a title and axis labels
Then write two sentences: how could someone misread these charts?
"""

import matplotlib.pyplot as plt
labels = ["A"] * 80 + ["B"] * 20

count_a = labels.count("A")
count_b = labels.count("B")
plt.bar(["A","B"],[count_a, count_b])
plt.title("Class balance")
plt.xlabel("Class")
plt.ylabel("Number of samples")
plt.savefig("counts.png")
plt.close()



