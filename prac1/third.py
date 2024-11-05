lst = ['Ok', 1, True, 'Ok', 1, 1.2, True]

print('original list:', lst)

no_dup = []
used = set()

for elem in lst:
    if (elem, type(elem)) not in used:
        used.add((elem, type(elem)))
        no_dup.append(elem)

print('no duplicates:', no_dup)