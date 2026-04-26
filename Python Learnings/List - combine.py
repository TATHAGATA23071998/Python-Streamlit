# combining lists
l1 = [1, 2, 3]
l2 = [4, 5, 6]
combined = l1 + l2
print(combined)

mult = l1 * 2
print(mult)

l1.extend(l2)
print(l1)

nest_matx = [l1,l2]
print(nest_matx)

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d']
comb = list(zip(list1,list2))
print(f"The combined and paired list is: {comb} !")

