"""
Task 10 – Library Records:
Given a list of dictionaries books, where each book has the keys title, year and available, print the
title of every available book and then the title of the oldest book.
"""

books = [
    {"title":"Dune","year":1965,"available":True},
    {"title":"Neuromancer","year":1984,"available":False},
    {"title":"The Martian","year":2011,"available":True},
]

oldest = books[0]
for info in books:
    if info["available"] == True:
        print(f"Available: {info["title"]}")
    if info["year"] < oldest["year"]:
        oldest = info

print(f"Oldest book: {oldest["title"]}")
