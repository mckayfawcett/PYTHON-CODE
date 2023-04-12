'''This Code opens a file of Rosebowl winners, it creates a list using the information 
from the file. It will then run the list through several 
functions to determine the total wins each time has.'''

# ---------------------------------------------------------
# 4/11/23
# McKay Fawcett
# CSIS-1300-01-Sp23
# ---------------------------------------------------------

from collections import Counter
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here,'Rosebowl.txt')

def main():
    'This is Main'
    list_of_teams = updated_data(filename)

    infomration_request(list_of_teams)

    four_more(list_of_teams)

    number_of_wins(list_of_teams)




def updated_data(filename):
    'This functions reads the original file and adds to it.'

    #Use try-catch
    try:
        #opens 'Rosebowl.txt
        infile = open(filename,'r', encoding="utf-8")
        rosebowllist = [line.rstrip() for line in infile]
        infile.close()
        updated_winners = ["Oregon", "Stanford", "USC", "Georgia", "Ohio State", "Oregon", "Alabama", "Ohio State", "Penn State"]


    except FileNotFoundError:
        print("File not found.")
    rosebowllist.extend(updated_winners)
    return rosebowllist

def four_more(teams):
    'This takes the list_of_teams and rewrites it only including the teams that have won more than 4 times It then prints that new list.'
    count = 0
    four_or_more = []

    for items in teams:

        if items in four_or_more:
            continue

        count = teams.count(items)

        if count >= 4:
            four_or_more.append(items)

    print ("The teams with four or more wins are: ")

    for team in four_or_more:
        print (team)

def number_of_wins(list):
    'This function takes the list_of_teams puts it through a counter and prints the results.'
    total_wins = list
    #This is a subclass dictionary that counts objects and numbers them.
    total_winners = Counter(total_wins)
    print("\nThe following is each team and the number of total wins they have recived:")
    #most common takes a list and orders it.
    for key, c in total_winners.most_common():
        print("{}: {}".format(key, c))


#Creative Element: made a function that will tell a user how many times a team has won.
def infomration_request(list):
    'This function takes a user input of a team and will tell the user how many times a team has won'
    userinput = (input("Type the name of a Rosebowl winner to view how many times they have won: ")).capitalize()
    items_count =Counter(list)
    print("\n",userinput,"Has won",items_count[userinput], "time(s)\n")

main()

#This Program took me a lot longer than I thought it would. I Had a good start to it, but ran into a problem when I was trying to write a new file using the information of the old
# I kept checking the debugger to try to figure it out. For some reason I didn't work
# After serval hours of trial and error and tried my code again 
# from a different approch this time creating a list from the infomration on the file. 
# It worked much better. I even stumbled upon Counter when I was troubleshooting. that was really useful.