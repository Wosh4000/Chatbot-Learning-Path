import random

lengthpassword = int(input("Please enter the length of the password you require"))

password = ""

for i in range(lengthpassword):
    j = random.randint(1,4)
    if j == 1:
        password = password + str(chr(random.randint(63, 90)))
    elif j == 2:
        password = password + str(chr(random.randint(48, 57)))
    elif j == 3:
        password = password + str(chr(random.randint(97, 122)))
    elif j == 4:
        password = password + str(chr(random.randint(35, 37)))        

print(password)