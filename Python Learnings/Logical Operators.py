# Example of and operator
a = 5
b = 10
if a > 0 and b > 0:
    print("Both a and b are positive numbers.")


# Example of or operator
c = -5
d = 10
if c > 0 or d > 0:
    print("At least one of c or d is a positive number.")
    
# Example of not operator
e = 5
if not e < 0:
    print("e is not a negative number.")

# Sequence of logical operators
f = 5
g = -10
if (f > 0 and g < 0) or (f < 0 and g > 0):
    print("f and g have opposite signs.")

### Task1: Allow the access if the user is logged in or they are guest but they must not be banned.
is_logged_in = True
is_guest = True
is_banned = False
if((is_logged_in or is_guest) and not is_banned):
    print(f"Access granted")
else:    print(f"Access denied")

### Task2: 
#1. Check if a user's name is not empty and the age is greater than equal to 18
name = "abc"
age = 20
if name != "" and age >= 18:
    print("User is valid.")
else:    print("User is invalid.")

#2. Check if the password is 8 characters and has no spaces
password = "passw0rd"
if len(password) >= 8 and " " not in password:
    print("Password is valid.")
else:    print("Password is invalid.")

#3 Check if email is not empty, has @ and ends with .com
email = "tathagata4059@gmail.com"
if email != "" and "@" in email and email.endswith(".com"):
    print("Email is valid.")
else:    print("Email is invalid.")

# 4. Check if an username is stirng, not none and has at longer than 5 characters
username = "abc12345"
if isinstance(email,str) and not None and len(username) > 5:
    print("Username is valid.")
else:    print("Username is invalid.")

#5. Check if the user is either an admin or a moderator and either they are not banned or they have a verified emails
is_admin = True
is_moderator = True
is_banned = True
is_verified = True
if (is_admin or is_moderator) and (not is_banned and is_verified):
    print ("Access given")
else: print ("Access revoked")