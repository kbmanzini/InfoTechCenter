print("\n****************************\n")

print("Weather Branch - Developer:KB Manzini")

#Import Libraries HERE!
import random
from time import sleep

# Weather Function to determine the weather
def weather():
    weatherForcastList = ["snowing", "blizzarding", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForcastList)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowing":
        print ("\nThe National Weather Service has updated our alarm by 30 minutes because "
        " it is ", weatherAlert, "right now.")
    elif weatherAlert == "blizzarding":
        print ("\nThe National Weather Service has updated our alarm by 60 minutes because "
        " it is ", weatherAlert, "right now.")

vehicleResponseSystem()