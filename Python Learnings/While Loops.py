i = 1
while (i < 4):
    print(i)
    i+=1

#answer = ""
#while answer != "yes":
#    answer = input("Do you agree Y/N: ")
#print("Ok")

while True:
    answer = input ("do you agree Y/N: ")
    if answer == 'yes':
        break
print("ok")


attempts = 0
while attempts <= 3:
    answer = input('do you agree Y/N: ')
    if answer == 'yes':
        print('ok')
        break
    attempts = attempts + 1
else:
    print('not ok')