''' A program to calculate how much caffeine remains in the body after a certain amount of time has passed. '''

# 2/8/23
# McKay Fawcett
# CSIS-1300-01-Sp23

# take the amount of caffeine and multiply it by 0.13
caffeineTotal = 130
absorptionRate = 0.13
caffeineLoss = caffeineTotal*absorptionRate
#subtract caffineLoss from caffineTotal = new caffineTotal
caffeineTotal = caffeineTotal-caffeineLoss
#define hours
hours = 1
#create a while loop that counts the number of hours until caffine is under a certain amount
while caffeineTotal > 65.0:
    caffeineLoss = caffeineTotal*absorptionRate
    caffeineTotal = caffeineTotal-caffeineLoss
    hours += 1
print("Less than ", round(caffeineTotal), "mg. will remain after", hours, "hours" )

#How much caffeine would be in the body after 24 hours
caffeineTotal = 130
hours = 0
while hours < 24:
    caffeineLoss = caffeineTotal*absorptionRate
    caffeineTotal = caffeineTotal-caffeineLoss
    hours += 1
print(round(caffeineTotal,2), "mg. will remain after", hours, "hours" )

#How much caffeine is left after continuous drinking for 24 hours
caffeineTotal = 130
hours = 0
while hours < 24:
    caffeineLoss = caffeineTotal*absorptionRate
    caffeineTotal = caffeineTotal-caffeineLoss
    hours += 1
    caffeineTotal += 130
print(round(caffeineTotal,3), "mg. will remain after", hours, "hours" )

#creative element: let user input an amount off caffeine, and will tell the user how many hours it will take for the caffeine to be completely absorbed.
hours = 1
userCaffeineTotal = int(input("\nEnter the total mg(s) of caffeine that is in your drink: "))
while userCaffeineTotal > 1:
     caffeineLoss = userCaffeineTotal*absorptionRate
     userCaffeineTotal = userCaffeineTotal-caffeineLoss
     hours += 1

print("it will take ", hours, "hours for the caffeine to be completely absorbed from your body!")
# sorry im turning this in late, I emailed you and never got a response. I played around with this again this morning, then I figured I try changing userCaffeineTotal > 0, to 1 and that fixed the problem.