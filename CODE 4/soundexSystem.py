'''A program that takes a word and assigns it a Code from the Soundex coding algorithm'''

# 2/15/23
# McKay Fawcett
# CSIS-1300-01-Sp23

# Get a word from a user 
word = input("\nPlease enter a word ")
# CREATIVE ELEMENT: only accept a single word, with no spaces or numbers or special characters
while not word.isalpha():
 print ("That is not a word! Please enter only alphabetical characters. Try again")
 word = input("\nPlease enter a word ") 
# make sure to put the word into all upper
word = word.upper()

#code takes the first letter of the word and stores it.
code = word[0]
counter =""
#Put word into for loop starting with the second letter, making sure to lower case all letters.
#this loop does not check for a, e, i, o, u, h, y, and w. it doesnt get added to the code and is excluded.
for ch in word[1:].lower(): 
    if ch in "bfpv" and counter!= '1': #starting with the second letter of the word check and see if it has any of the following.
       # add the number 1 to code
        code += '1' 
        # counter goes up and makes sure if their are double letters it moves past them.
        counter ='1'
    elif ch in "cgjkqsxz" and counter != '2':
        code +='2'
        counter = '2'
    elif ch in "dt" and counter != '3':
        code +='3'
        counter = '3'
    elif ch in "l" and counter != '4':
        code +='4'
        counter = '4'
    elif ch in "mn" and counter != '5':
        code +='5'
        counter = '5'
    elif ch == "r" and counter != '6':
        code +='6'
        counter = '6'
# The for loop contiunes to check for letters until there are only numbers left. Then print code.
# my original plan for this was to put it into a while loop and continually replace each letter of the word until the word because the correct code. However that changed after class.
# since im turning this in late i saw a few examples of other peoples codes and I changed my design after seening better iterations of the code.
print(code)