'''This program takes a word or phrase and reads it the same frowards and backward and determins if is the same.'''
import re
#--------------------------
# McKay Fawcett
# 2/25/23
# CSIS-1300-01-Sp23
#--------------------------


userInput = input("Enter a word or phrase: ")

#get rid of special characters and spaces and make lower
withoutSpec = re.sub('\W+', '', userInput.lower())

#get rid of numbers
withoutNum = re.sub('\d', '', withoutSpec)


palindrome = withoutNum[::-1]


if palindrome == withoutNum:
    print(userInput.upper(), "is a palindrome")
else:
    print("That is not a Palindrome!")
# added an option to see a palindrome poem i found
poem = input("Would you like to see a palindrome poem? Enter y or n: ")
x = poem.lower()
if x == 'y':
    print("""Dammit I’m mad.
Evil is a deed as I live.
God, am I reviled? I rise, my bed on a sun, I melt.
To be not one man emanating is sad. I piss.
Alas, it is so late. Who stops to help?
Man, it is hot. I’m in it. I tell.
I am not a devil. I level “Mad Dog”.
Ah, say burning is, as a deified gulp,
In my halo of a mired rum tin.
I erase many men. Oh, to be man, a sin.
Is evil in a clam? In a trap?
No. It is open. On it I was stuck.
Rats peed on hope. Elsewhere dips a web.
Be still if I fill its ebb.
Ew, a spider... eh?
We sleep. Oh no!
Deep, stark cuts saw it in one position.
Part animal, can I live? Sin is a name.
Both, one... my names are in it.
Murder? I’m a fool.
A hymn I plug, deified as a sign in ruby ash,
A Goddam level I lived at.
On mail let it in. I’m it.
Oh, sit in ample hot spots. Oh wet!
A loss it is alas (sip). I’d assign it a name.
Name not one bottle minus an ode by me:
“Sir, I deliver. I’m a dog”
Evil is a deed as I live.
Dammit I’m mad.""")
else:
    print("Dang thats lame")

# this wans't to hard of a program, honeslty i wasn't sure what to do the creative element. That took me the longest to figure out. but I finally decided. 
# the beggining also took me a minute as I kept running into problems.