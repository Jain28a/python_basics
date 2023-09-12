set1 = {1, 2, 3, 4, 4, 4}
print(set1)

set1.add(55)
print(set1)

set2 = {3, 4, 5, 6}
print(set1.union(set2))
#print(set1.intersection(set2))
print(set1.difference(set2)) #common + from set1
print(set1.symmetric_difference(set2))