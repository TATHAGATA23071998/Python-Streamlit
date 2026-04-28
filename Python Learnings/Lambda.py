multiply = lambda x,y:x*y
print(multiply(5,6))

checking = lambda x: True if x%2==0 else False
print(checking(5))

string = lambda i: i in 'Python'
print(string('P'))

prices = [' $5.00', '$10.00', '$15.00']
store = list(map(lambda p: float(p.replace('$', '').strip()), prices))
print(f"the final values are: {store}")

pricing_list = [100, 80, 150, 60, 220]
pl = list(filter(lambda p: p >= 100,pricing_list))
print(f"the final values are: {pl}")

students = [['John', 85], 
            ['Alice', 92], 
            ['Bob', 78], 
            ['Eve', 90]]
stu = list(filter(lambda row:row[1] >= 80, students))
print(f"the final values are: {stu}")

# Task
students1 = [['John', 85], 
            ['Alice', 92], 
            ['Bob', 78], 
            ['Eve', 90]]
stu1 = list(filter(lambda row:row[0].startswith('A') or row[0].startswith('B'), students1))
print(f"the final values are: {stu1}")