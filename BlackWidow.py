print("\n****************************\n")

print("Weather Branch - Developer:KB Manzini")

#Import Libraries HERE!
import random
from time import sleep

# Weather Function to determine the weather
def weather():
    weatherForcastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForcastList)
    return weatherCondition

print(weather())