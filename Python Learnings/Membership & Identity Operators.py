# Membership Operators
print ("f" in "Python")
print(3 not in [1,2,3])

# Validate that domain is not in the banned list
domain_name = "@gmail.com"
is_banned = ["@spam.com", "@xyz.com", "@bot.net"]
if domain_name in is_banned:
    print("Hacked")
else: print ("Safe")

# Identity operators
x = ['A', 'B', 'C']
y = ['A', 'B', 'C']
print(x==y)
print(x is y)

abc = 10
d = 10
print(abc is d)

# Validate the email address. It must be filled and not empty
email = "abc@gmail.com"
if(email is not None and email != "" and email != " " and "@" in email and email.endswith(".com")):
    print("valid")
else: print("invalid")