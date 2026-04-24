# adding items to list
letters = ['a', 'b', 'c', 'd', 'e']
letters.append('f')
print(letters)

letters.insert(1, 'x')
print(letters)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[2].append(10))
print(matrix[0].insert(3,4))
print(matrix)

# removing items from list
l = [1,2,3,4]
l.clear()
print(l)

li = [1,2,3,4,5,6,6]
li.remove(6)
print(li)

list_pop = [1,2,3,4,5,6,7]
removed_item =list_pop.pop(5)
print(list_pop.pop(5))
print(f"The removed value is: {removed_item}")

nmtx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
nmtx[1].remove(5)
print(nmtx)
nmtx[2].pop(0)
print(nmtx)

# updating items in list
lst = ['a', 't', 'u', 'b']
lst[0] = 'x'
lst[1] = 'y'
lst[2] = 'z'
lst[3] = 'w'
print(lst)
print(type(lst))

new_mtx = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
new_mtx[0][0] = 10
new_mtx[1][1] = 11
new_mtx[2][2] = 12
print(new_mtx)
