# Iterate through a list and then store it in a new list
lists1 = [' a', 'b ', 'c ', 'd', ' e']
new_list = []
for list in lists1:
    new_list.append(list.replace('e','x').upper().strip())
print(new_list)

lists2 = [' a', 'b', 'c', 'd', ' e']
for list2 in enumerate(lists2):
    print(list2)

lists3 = ['a', 'b', 'c', 'd', 'e']
for list in reversed(lists3):
    print(list)

l = ['a', 'b', 'c', 'd', 'e']
n = [1, 2, 3, 4, 5]
for l,n in zip(l, n):
    print(l,n)

names = ['John', ' Jane', 'Doe']
for name in map(str.strip, names):
    print(name)

numbers = ['1', '2', '3', '4', '5']
for number in map(int, numbers):
    print(number)

letters = ['a', 'b', 'c', 'd', 'e']
for letter in map(str.upper, letters):
    print(letter)

new_list = ['a', 'b', 'c', 'd', 'e', '10', 'None', 'True', 'False']
for item in filter(str.isalpha, new_list):
    print(item)