# Types
x = 5
y = 3.14
z = 5 + 7j
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'complex'>

a = 10
a1 = float (a)
print(a1)

b = 6 
c = 7
d = complex(b, c)
print(d)

# Arithmetic Operators
x = 2
y = 3
a = x * y
b =+ a
c = -a
d = x// y
e = x% y
f = x/y
g = x+y
h = x-y
print(a)  # Output: 6
print(b)  # Output: 6
print(c)  # Output: -6
print(d)  # Output: 0
print(e)  # Output: 2
print(round(f,2))  # Output: 0.67
print(g)  # Output: 5
print(h)  # Output: -1

# Rounding Numbers
import math
x = 5
y = 10
z = 3.14159
print(round(x))  # Output: 5
print(round(y))  # Output: 10
print(round(z, 2))  # Output: 3.14
print(abs(x-y))
print(math.ceil(z))
print(math.floor(z))
print(math.trunc(z))

## Adbvanced Math Functions
import math
x = 16
y = 25
a = math.sqrt(x)
b = math.sin(x/y)
c = math.cos(x/y)
d =math.log(x)
print(a)  # Output: 4.0
print(round(b, 4))  # Output: 0.5878
print(round(c, 4))  # Output: 0.587
print(round(d, 4))  # Output: 2.7726

# Random Numbers
import random
x = random.randint(1, 10)
y = random.random()
print(x)  # Output: A random integer between 1 and 10
print(y)  # Output: A random float between 0 and 1


## Validation
x = 7.0
y = 7.1
print(isinstance(x, int))  # Output: False
print(isinstance(x, float))  # Output: True
print(isinstance(y, int))  # Output: False
print(isinstance(y, float))  # Output: True
print(x.is_integer())
print(y.is_integer())

# Task
import math
x = random.randint(1,100)
if(x%2 == 0):
    print(f"{x} is an even number")
else:
    print(f"{x} is an odd number")