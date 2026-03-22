#This variable takes the password the user wants to check as a variable
Password = input("What is your password? ")

#This checks the password in the rockyou.txt file
with open ("rockyou.txt" ,"r", encoding = "latin-1") as rockyou:
    found = False
    for line in rockyou:
        if Password == line.strip():
            found = True                
            break                                                   #stop if the password is found in rockyou.txt

if found:
    print("Your password has been found.")
else:
    print("Your password is safe.")     