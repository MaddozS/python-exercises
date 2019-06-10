list = [3,4,3,3,2,4,5]
uniques = []
for item in list:
    if item not in uniques:
        uniques.append(item)
print(uniques)