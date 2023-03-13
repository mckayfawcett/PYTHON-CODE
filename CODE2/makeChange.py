''' A program to make change from an amount of money from 0 through 99 cents
input by the user. The output of the program should show the number of coins
from each denomination used to make the change.'''

# 1/30/23
# McKay Fawcett
# CSIS-1300-01-Sp23

# get input of 0-99 from the user
inputNumber = int (input("\n\nEnter a number between 0 - 99: "))

# CREATIVE ELEMENT:added a while statment that makes sure the user keeps the number between 0-99
while inputNumber > 99 or inputNumber < 0:
    inputNumber = int (input("\nTry again, Enter a number between 0 - 99: "))

# divide inputNumber by 25 to get number of quarters
quarters = 25
print("Number of Quarters is:", inputNumber//quarters)

# mod inputNumber by 25 to get the remaining amount
pennies = inputNumber%quarters
print("Number of pennies is: ",pennies)

# divide inputNumber by 10 to get number of dimes
dimes = 10
print ("\nNumber of Dimes is: ", inputNumber//dimes)

# mod inputNumber by 10 to get the remaining amount
pennies = inputNumber%dimes
print("Number of pennies is: ",pennies)

# divide inputNumber by 5 to get number of nickles
nickels = 5
print ("\nNumber of nickles is: ", inputNumber//nickels)

# mode inputNumber by 5 to get the pennies
pennies = inputNumber%nickels
print("Number of pennies is: ",pennies)

#I liked this program it is pretty simple. Not sure if you wanted to take the change from the quarts and contiue it through the dimes and nickels.