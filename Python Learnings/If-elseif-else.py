# if - else_if - else
M = float(input("Enter your marks: "))
if (M >= 90):
    print("Good")
elif (M <= 90 and M >= 80):
    print("Medium")
else:
    print("Bad")

# Nested ifs
score = 90
submitted_project = True
if (score >= 90):
    if (submitted_project):
        print("A+")
elif (score <= 90 and score >= 80):
    print("A")
elif (score <= 80 and score >= 70):
    print("B")
elif (score <= 70 and score >= 60):
    print("C")
elif (score <=60 and score >=50):
    print("D")
elif(score <=50 and submitted_project):
    print("ok")
else:
    print("F")

# independent ifs
marks = 50.2
project_submission = True

if(marks > 50):
    print("Pass")
else:
    print("Fail")

if (project_submission is True):
    print("Yes")
else:
    print("No")

# Task 1:
# Validate the correctness and quality of emails:
#(a) Must not be empty
#(b) Must contain '.' and only one @
#(c) Must end with .com, .org or .net
#(d) Must not be longer than 254 characters
#(e) Must start and end with a letter or digit

email = "tathagata4059@gmail.com"

if (email is None and email == "" and email == " "):
    print ("Invalid")
elif not ("@" in email and "."in email and email.count("@") == 1):
    print("Invalid_1")
elif not (email.endswith(".com") or email.endswith(".org") or email.endswith(".net")):
    print("Invalid_2")
elif (len(email)>254):
    print("Invlaid_3")
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Invlaid_4")
else:
    print("Valid")

# Task 2:
# Validate the correctness of the passwords:
# (a) Must not be empty
# (b) Must be atleast 8 characters
# (c) Must incluse atleast 1 uppercase and 1 lowercase character
# (d) Must not be the same as email
# (e) Must not contain any spaces
# (f) Must start and end with a letter or a digit

password = "Tathagata123"
email_id = "tathagata4059@gmail.com"

upper_count = sum(1 for ch in password if ch.isupper())
lower_count = sum(1 for ch in password if ch.islower())

if password is None or password.strip() == "":
    print("INVALID_1")
elif len(password) < 8:
    print("INVALID_2")
elif not (upper_count >= 1 and lower_count >= 1):
    print("INVALID_3")
elif password == email_id:
    print("INVALID_4")
elif not (password[0].isalnum() and password[-1].isalnum()):
    print("INVALID_5")
else:
    print("VALID")
