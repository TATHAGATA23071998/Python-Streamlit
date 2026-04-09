# String categories

# Type
## str, type
name = 'Tathagata Chakraborty'
age = 27
print (type(name))
print (str(name))
print(type(age))
print ("age is:" + str(age))

age = str(age)
age = age + "5"

print(age)

# Mathematical operations on strings
name = input("Enter your name: ")
if len(name) < 10:
    print("Name is ok")
else:
    print("Name is long")

name = """Python is a high level programming language. 
          \tPython has various applications. 
          \tPython is easy to learn."""
print(name.count('Python'));
print(name);


# Transformations
## replace
price1  = '1234/56'
print (float(price1.replace("/",".")))

print(type(float(price1.replace("/","."))))
      
price_2 = '$1,234.56'
print(float(price_2.replace("$","").replace(",","")))

## task
ph_no = "+49 (176) 123-4567"
cleaned_ph_no = ph_no.replace("+","00").replace(" ", "").replace( " ", "").replace("(", "").replace(")", "").replace(" ", ""). replace("-", "")
print(cleaned_ph_no)

### + operator that joins two strings
first_name = "Tathagata"
last_name = "Chakraborty"
full_name = first_name + " " + last_name
print(full_name)

### f string
first_name = "Tathagata"
last_name = "Chakraborty"
is_student = True
age = 27
height = 1.75
print(f"My name is {first_name} {last_name}. I am {age} years old. I am a student: {is_student}. My height is {height} in mts.")
print(f"{2 + 3} = 2+3 is good")

### .split () method
stamp = "2026-09-20 14:30:10"
new_stamp = stamp.split(" ")
new_stamp_1 = new_stamp[0].replace("-","/")
print(f"The \'cleaned version\'of the dates is: {new_stamp_1} and {new_stamp}")

### * operator
value = "Python"
print(f"Python is {value*3}")

### Indexing and slicing with []
name = "2026-09-20"
var_1 = name[0:4] # extractng the year
var_2 = name[5:7] # extracting the month
var_3 = name[8:10] # extracting the day
print(f"The year is {var_1}, the month is {var_2} and the day is {var_3}")

### Data cleaningmfunctions
## strip() methods
name = "   Tathagata Chakraborty   "
var_1 = len(name)
var_2 = name.strip () # removes the leading and trailing spaces
print(f"The length of the name is: {var_1}")
print(f"The cleaned name is: {var_2}")
print(f"{len(var_2)}")

## upper and lower cases
name = "  Tathagata Chakraborty  "
print(name.upper().strip())
print(name.lower().strip())

### Task
text = " 968-Maria, (D@t@ Engineer );; 27y"
Name = "968-Maria,"
Role = " (D@t@ Engineer  );;"
Age = "27y"
cleaned_text = "name: " + Name.lower().replace("968-", "").replace(",", "") +  " | "  + "role: " + Role.replace("@", "a").replace(";;" ,"").lower().replace("(", "").replace(")", "").strip() +  " | " +"age: " + Age.replace("y", "years")
print(f"The cleaned text is: {cleaned_text}")


# Single line extraction
text = " 968-Maria, (D@t@ Engineer );; 27y"
print(f"name: {text.split('-')[1].split(',')[0].strip().lower()} | role: {text.split('(')[1].split(')')[0].replace('@', 'a').strip().lower()} | age: {text.split(';;')[1].replace('y', '').strip()}")

### Search functions
var_1 = "2026- Feb- 10"
print(var_1.startswith('2026'))
print(var_1.endswith('30'))
print(var_1.find('Feb'))
print('Feb' in var_1)
print('Feb' not in var_1)


phone = "+49-176-1234567"
print(phone[phone.find("-")+1:])