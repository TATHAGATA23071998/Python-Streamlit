#1. Using the assignment operator '='
org_list = [1,2,3,4]
new_list = org_list.insert(0,'x')
new_list = org_list
print(org_list)
print(new_list)

#2. Shallow copy using '.copy()' method
shl = ['a', 'b', 'c', 'd']
shl_copy = shl.copy()
shl_copy.append('e')
shl_copy.insert(2,10)
shl_copy.pop(0)
shl_copy.reverse()
print(shl)
print(shl_copy)

matrix = [['a', 'b', 'c', 'd'],
           ['e', 'f', 'g', 'h']]
shl_mtx_copy = matrix.copy()
shl_mtx_copy[0][1] = 10
print(matrix)
print(shl_mtx_copy)

# Deep copy using the 'deepcopy()' function
import copy
matrix_deep = [['a', 'b', 'c', 'd'],
                ['e', 'f', 'g', 'h']]
mtxd = copy.deepcopy(matrix_deep)
mtxd[0].insert(1,'x')
print(matrix_deep)
print(mtxd)

# is operator
copy1 = matrix
print(copy1 is matrix)
print(copy1[0] is matrix[0])

copy2 = matrix.copy()
print(copy2 is matrix)
print(copy2[0] is matrix[0])

copy3 = copy.deepcopy(matrix)
print(copy3 is matrix)
print(copy3[0] is matrix[0])