"""
Save the data below as expenses.csv Then, with pandas:
1. Read the file and check that it has the coulmns department and expense.
2. Remove the row where expense is negative
3. For each department, print the count, total and average expense.
"""

import pandas as pd

df = pd.read_csv("expenses.csv")
df = df[df["expense"] > 0]
groups = df.groupby("department")
groups = groups["expense"].agg(["count","sum","mean"])
print(groups)


"""
Slayttaki çözüm
import pandas as pd
df = pd.read_csv("expenses.csv")

required = {"department","expense"}
if not required.issubset(df.columns):
    print("Missing columns)
df = df[df["expense] >= 0]
summary = df.groupby("department")["expense"].agg(["count","sum","mean"])
print(summary)

"""
