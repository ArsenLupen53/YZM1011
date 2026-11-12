"""
One score is missing (None). For each group, print:
1. how many scores are present
2. how many scores are missing
3. the average of the present scores
Then answer: what happens to group A's average if the missing score is filled with 0?
"""

import pandas as pd
df = pd.DataFrame({"group":["A","A","B","B"],
                   "score": [80,None,50,90]})

group = df.groupby("group")["score"]

counts = group.count()
missing = group.size() - counts
means = group.mean()

for g in counts.index: #burda means.index yapsak da olur counts şöyle [1,2]
    print(f"{g}: count={counts[g]},",
          f"missing={missing[g]},",
          f"mean={means[g]}")