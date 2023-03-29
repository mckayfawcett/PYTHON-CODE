'''This Program displays the number of numbers in the file Numbers.txt and also chooses the largest and smallest number in the file.'''


# ---------------------------------------------------------
# 3/27/23
# McKay Fawcett
# CSIS-1300-01-Sp23
# ---------------------------------------------------------


# This is main used
def main():
    'This is the main function'
    file = 'Numbers.txt'
    numbers(file)
    maximum(file)
    minimum(file)
    average(file)


def numbers(file):
    'this is used to determine the total number of numbers in the txt file.'
    infile = open(file, 'r', encoding="utf8")
    count = 0
    for line in infile:
        # this ignors white spaces or extra lines
        if line != "\n":
            count += 1
    print(count)
    infile.close()


def maximum(file):
    'Used to determine the maxium number in the file.'
    infile = open(file, 'r', encoding="utf8")
    max = 0
    for line in infile.readlines():
        num = int(line)
        if max < num:
            max = num
    print(max)
    infile.close()


def minimum(file):
    'This Functions finds the minimum number in the txt file.'
    infile = open(file, 'r', encoding="utf8")
    min = 100
    for line in infile.readlines():
        num = int(line)
        if num < min:
            min = num
    print(min)
    infile.close()


# CREATIVE ELEMENT: made a function to be able to determine the total average of all the numbers in the file
def average(file):
    'This function determines the total average of the numbers in the file'
    infile = open(file, 'r', encoding="utf8")
    average = 0
    divide = 0
    for line in infile.readlines():
        num = int(line)
        average += num
        divide += 1
    total_average = int(average/divide)
    print(total_average)
    infile.close()


main()

# this program wasn't to challanging. The real issue I ran into was trying to get the program to read the file.
# Once I figured that out I was able to make the program pretty quick.
