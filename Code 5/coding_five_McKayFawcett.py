'''This program is asks the user to input an intital height in feet, and an initial velocity (feet poer second). 
It then calculates the maximum height of the ball
and then determines when the ball will hit the ground.'''

# 3/13/23
# McKay Fawcett
# CSIS-1300-01-Sp23





#This is the main function
def main():

    print("Please note that the following will be calcualted in feet.")
    #call getInput function
    intH, intV = getInput()

    #call maximumHeight function
    maximumHeight(intH,intV)
    
    ground = timeToGround(intH,intV)
    print("The ball will hit the ground after approximately ", ground, "seconds.")
    momentum = calculateMomentum(intV)
    print("The ball will have a momentum of ", momentum, "pounds ft/s.")













#def getInput has a user input their initial height and velocity of the ball
def getInput():
    #get height of ball from the user
    #get velocity of ball from user

    height = int (input("Enter the initial height of the ball: "))
    velocity = int (input("Enter the initial velocity of the ball: "))
    
    #call isValid function
    if isValid(height, velocity):
        return height, velocity
        
    #if the input is not valid
    print("That is not a valid input")


# Check to see if the inputs are valid.
def isValid(h,v):
    if  h > 0 and v > 0:
        return True
    else:
        return False

#Calculate the maximum height that the ball will reach.
def maximumHeight(height, velocity):
    
    maxHeight = float (height + (velocity * (velocity/32)) - (16 * ((velocity/32) ** 2)))
    print("The maximum height of the ball is ", round(maxHeight,2)," feet.")
    return round(maxHeight,2)

# calculate the time it takes the ball to hit the ground
def timeToGround (height, velocity):
    time = 0.01
    while True:
        ballheight = (height + (velocity * time) - (16 * ((time) ** 2)))
        if ballheight <= 0:
            break
        else:
            time += 0.01
    return round(time,2)

#CREATIVE Element: calculate the momentum of the ball in kg/s.
def calculateMomentum(velocity):
    mass = int (input("Enter the mass of the ball in pounds: "))
    momentum = (mass * velocity)
    return momentum

# main
main()

# this program was really tough for me, it took me a while to actually get the github to work, then when i finally started to code, the functions were confusing to me.
# im glad i finally got it, even after such a long time.
