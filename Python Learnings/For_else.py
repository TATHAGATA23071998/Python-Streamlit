ranges = [1,2,3]

for range in ranges:
    print(f"the range is: {range}")
else:
    print("done")


items = [1,2,3,4,5,6,7]
for item in items:
    if (item%2 == 0):
        print(item)
        break
else:
    print("Odd")

# Search and validate
names = ['A', 'B', None, 'C']
for name in names:
    if name in ('',' ',None):
        print(f"{name}")
        break
    else:
        print(f"empty")

files = ['abc.csv', 'def.csv', 'ghi.excel']
for file in files:
    if ('.csv' not in file):
        print (f"invalid:{file}")
        break
    else:
        print("valid")

# task
files = ['report.csv', 'data.xlsx', 'summary.docx', 'report.csv', 'data.csv']

for file in files:
    if file.count(file) > 1:
        print("duplicates")
        break
else:
    print('unique')