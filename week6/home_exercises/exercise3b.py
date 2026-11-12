"""
Make two charts and save each one as a PNG file:
2. scores.png: a histogram of the scores
Give both charts a title and axis labels
Then write two sentences: how could someone misread these charts?
"""

import matplotlib.pyplot as plt
scores = [45,75] * 45 + [55,85] * 35 + [65] * 20
plt.hist(scores, bins=[40,50,60,70,80,90])
plt.title("Score distribution")
plt.xlabel("Score intervals")
plt.ylabel("Freqeuncy")
plt.savefig("scores.png")
plt.close()