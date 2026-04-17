# Break
names = ['A', 'B', '', 'C']
for name in names:
    if (name == ''):
        print(f'name is empty')
        break
    print (f'name is {name}')

# Continue
    names = ['A', 'B', '', 'C']
for name in names:
    if (name == ''):
        print(f'name is empty')
        continue
    print (f'name is {name}')

# Pass
names = ['A', 'B', '', 'C']
for name in names:
    if (name == ''):
        print(f'name is empty')
        pass
    print (f'name is {name}')

# Task 1: Loop through the days and print only working days, skipping the weekends
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for day in days:
    if day in ['Saturday', 'Sunday']:
        print(f"{day} is a Weekend")
        continue
    print(f"day is {day}")

# Task 2: Scan emails to restrict unwanted data from entering the system
emails = ['abc@gmail.com', '123@yahoomail.com', 'DROP TABLE USERS', '#$&@rediffmail.com']
for email in emails:
    if '@' '.com' not in email:
        print ("Data not safe")
        break
    print(f"email is: {email}")