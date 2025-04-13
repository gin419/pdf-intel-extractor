text = input("Enter a string: ")
counts = {}
for c in text:
    counts[c] = counts.get(c, 0) + 1
print(counts)
