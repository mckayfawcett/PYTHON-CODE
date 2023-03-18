''' This program takes a string input. It then checks that input to see if there are 
three consecutive letters that are also consecutive in the alphabet.'''



#---------------------------------------------------------
# 3/18/23
# McKay Fawcett
# CSIS-1300-01-Sp23
#---------------------------------------------------------


#This is the main function, used to call the other functions
def main():
    '''This is main'''
    word =get_input()
    #This makes sure the word is all lower case
    tripleword = word.lower()
    is_triple_consecutive(tripleword)
    #CREATIVE ELEMENT pt.1 added a Boolean so that if it returns true they will get this message
    if bool(tripleword):
        print(word, "contains three successive letters in consecutive alphabetical order")












def get_input():
    """ get an string from the user"""

    word = input("Enter a word: ")
    if is_valid(word):
        return word

# Creative Element pt 2: This function checks to make sure that the word doesn't
# contain any letters.
def is_valid(word):
    '''Checks for word'''
    if  any(i.isdigit() for i in word) :
        return False
    else:
        return True


# This function takes the characters in a word and checks to
#  see if they are consecutive in the alphabet.
def is_triple_consecutive(input_word):
    '''Checks for 3 in a row'''
    for i in range(0,len(input_word) -2,1):
#Here i wanted to get it to print out the 3 letters that
#  were consecutive, but I couldn't figure it out.
        if input_word[i] < input_word[i +1] < input_word[i+2]:
            return True
        else:
            print("That word has no consecutive letters")
            return False


#This is main
main()
#This program took me a bit becasue ive been behind on other stuff in class. During this program
# I learned that because a function returns a value,
#If you set that value to return True or false, you can then
# just put that value into a Boolean, which I didn't know.
