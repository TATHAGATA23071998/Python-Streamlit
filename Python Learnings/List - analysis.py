numbers = [1,2,3,4,5,5,6,7,8,9,10]
print(f"maximum is: {max(numbers)}")
print(f"minimum is: {min(numbers)}")
print(f"total is: {sum(numbers)}")
print(f"average is: {sum(numbers)/len(numbers)}")
print(f"length is: {len(numbers)}")

print(any([0, 0, 0, 1]))
print(all([0, 0, 0, 1]))
print(any(numbers))
print(all(numbers))

print(f"counting for 5 is: {numbers.count(5)}")
print(f"index of 5 is:{numbers.index(5)}") # returns the position of first occurence

print(f"existance:{11 in numbers}")
print(f"existance:{11 not in numbers}")

new = list(range(1,15)) # [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(new == numbers)
print(new > numbers)
print(new < numbers)
print(new is numbers)