''' this pgram ask for a fullname and spits it up'''
#--------------------
#  NAME
# DATE  
# COURSE
#-------------------

# using input function to get full name
fullName = input("Enter a full name: ")

# get the space on back of string using rfind 
backSpace = fullName.rfind(" ")

# my creative element get space for middle name
frontSpace = fullName.find(" ")

# print out names
print("Last name:", fullName[backSpace+1:])
print("Middle name:", fullName[frontSpace+1:backSpace])
print("First name:", fullName[:frontSpace])


#----------
# THOUGHTS?