count = 0
for i in (1,2,3,4,5):
    count = count + 1
    print(i)

# More polished
count = 0
items = (1,2,3,4,5,6) # tuple sequence
for item in items:
    count += count
    print(f"The rounds are:{item}")


count = 0
itmes = [1,2,3,4,5,6, "Hello"]
for item in itmes:
    count += count
    print(f"The new rounds are:{item}")

count = 0
items = "Analysis"
for item in items:
    count += count
    print(f'The values are:{item}')

for item in range (1,12):
    if (item % 2 != 0):
        print(item)

# Product
scores = [80, 50, 60, 75]
product = 1
for score in scores:
    product = product * score
    print (f"The total scores: {product}")

# Sum
scores = [80, 50, 60, 75]
sum = 0
for socre in scores:
    sum = sum + score
    print(f"{sum}")

# Task1
tables = range(1,11)
n = 7
for table in tables:
    new_table = n * table
    print(f"{n} x {table}={new_table}")

# Task 2
stars = range (1,7)
n = "*"
for star in stars:
    new = n * star
    print(f"{new}")