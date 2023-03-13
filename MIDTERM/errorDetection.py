import re
'''The purpose of this program is to determine if a Card number that someone has entered is a vaild card number.'''
#--------------------------
# McKay Fawcett
# 2/25/23
# CSIS-1300-01-Sp23
#--------------------------


# Validate a credit card number.
i = 0
num = input("Enter a credit card number: ")

#added a while loop so that if the customer gets the number wrong they can try again.
while i < 1:

 evenSum = 0
 oddSum = 0
 for i in range(0, len(num), 2):
    digit = int(num[i]) * 2
    if digit >= 10:
        digit -= 9
    evenSum += digit
 for i in range(1, len(num) + 1, 2):
    oddSum += int(num[i])

    # now it checks if it fits any of the 4 options becuase many cards have different lengths.
 if (evenSum + oddSum) % 10 == 0 and len(num) == 14:
    print("The number is valid.")
 elif (evenSum + oddSum) % 10 == 0 and len(num) == 15:
    print("The number is valid.")
 elif (evenSum + oddSum) % 10 == 0 and len(num) == 16:
    print("The number is valid.")    
 else:
    print("The number is not valid.")

 #creative element #2 added a way to check what type of card it is. 
 visa = re.search("^4[0-9]{12}(?:[0-9]{3})?$", num)
 mastercard = re.search("^5[1-5][0-9]{14}$", num)
 discover = re.search("^6(?:011|5[0-9]{2})[0-9]{12}$", num)
 diners = re.search("^3(?:0[0-5]|[68][0-9])[0-9]{11}$", num)
 jcb = re.search("^(?:2131|1800|35\\d{3})\\d{11}$", num)

 if visa:
    print ("You have a Visa Card")
    i += 1
 elif mastercard:
    print ("You have a Master Card")
    i += 1
 elif discover:
    print("You have a Discover Card")
    i += 1
 elif diners:
    print("You have a Diners Card")
    i += 1
 elif jcb:
    print("You have a JCB Card")
    i += 1
 else:
    print("try again")
    num = input("Enter a credit card number: ")
    i = 0

    # I used in the class example as my base, I then had to learn about the RegEx function or re. which allows me to search for something specific in an int or string.
    #I also had to learn about the formulas to determine the types of card, though american express uses a different system and i couldn't make it work with this one
    # This was a good program to learn aobut.