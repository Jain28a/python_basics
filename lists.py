list1 = [13, 21, 3, 43 ,5, 67, 7]
print(list1)
# Add items in list using append, extend, insert
#list1.append((2,0))
#list1.extend((4,5))
#list1.insert(7, 'example')
#print(list1)
#Remove items using del, pop, remove 
#del list1[3]
#print(list1)

#a = list1.pop(3)
#print(a)

#list1.remove(1)
#print(list1)

#Access list items
#print(list1[0:2])
#print(list1[0:10:2]) #skip evey second
#print(list1[::-1]) #print in reverse

# sort
print(sorted(list1))
list1.sort(reverse=True)
print(list1)
print(list1.index(3))
print(list1.count(5))