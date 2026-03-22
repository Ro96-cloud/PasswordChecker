#This variable takes the password the user wants to check as a variable
Password = input("What is your password? ")

#This checks the password in the rockyou.txt file
with open ("rockyou.txt" ,"r", encoding = "latin-1") as rockyou:        #Opens rockyou.txt in the same folder
    found = False                                                       #Default found variable is false
    for line in rockyou:                                                #Crawls through the lines in rockyou.txt
        if Password == line.strip():                                    #Checks if variable password is in the lines of rockyou.txt. Also strips the lines of whitespaces.
            found = True                                                #Changes found to true if password is in rockyou.txt              
            break                                                       #Stops the loop

if found:
    print("Your password has been found.")
else:
    print("Your password is safe.")     