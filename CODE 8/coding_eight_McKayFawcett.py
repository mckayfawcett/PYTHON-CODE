'''This program displays the states and their captials if they start with the same letter.
This program also asks the user for an input of the state and displays the abbreviation, nickname and captial of the state.'''

# ---------------------------------------------------------
# 4/4/23
# McKay Fawcett
# CSIS-1300-01-Sp23
# ---------------------------------------------------------


import os.path
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'StatesANC.txt')


def main():
    'This is main'

    print("The following are all the states and their capitals, only if they start with the same letter.")
    same_letter_state(filename)
    input_state(filename)
    input_number(filename)


def same_letter_state(filename):
    'This function displays states and their capitals from the file, only if they start with the same letter'
    infile = open(filename, 'r', encoding="utf8")
    for line in infile:
        # this line of code is used to add things into lists if its seperated by a comma.
        data = line.split(",")
        letter = data[0][0:1]
        if data[3].startswith(letter):
            print((data[3].rstrip()) + ",", data[0])
    infile.close()


def input_state(filename):
    'This function asks the user to input a state name and it displays revelvant information about that state.'
    userinput = input("Enter the name of a state: ")
    state = userinput.lower().capitalize()
    infile = open(filename, 'r', encoding="utf8")
    found = False
    state_data = infile.readline()
    # This contiunes to read each line, until true and ignores white space
    while (found == False) and (state_data != ""):
        data = state_data.split(",")
        if data[0] == state:
            print("Abbreviation:", data[1])
            print("Nickname:", data[2])
            print("Captial:", data[3].rstrip())
            # prints all data and changes to True, which takes us out of the loop
            found = True
        state_data = infile.readline()
    infile.close()


def input_number(filename):
    'This function asks the user to input a number and is will display all the states with that number of letters in is name'
    userinput = int(input("Enter a number "))
    infile = open(filename, 'r', encoding="utf8")
    for line in infile:
        data = line.split(",")
        state_number = data[0]
        if len(state_number) == userinput:
            print(data[0])
    infile.close()


main()
