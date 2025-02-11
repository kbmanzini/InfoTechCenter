# Print a decorative header
print("\n****************************\n")
print("Weather Branch - Developer: KB Manzini")

# Import necessary libraries
import random  # Used to generate random weather conditions
from time import sleep  # (Currently unused, but can be used for delays)

# Function to determine the weather condition randomly
def weather():
    # List of possible weather conditions
    weatherForcastList = ["snowing", "blizzarding", "icy", "rainy", "windy", "sunny"]
    # Randomly select one weather condition from the list
    weatherCondition = random.choice(weatherForcastList)
    return weatherCondition  # Return the selected weather condition

# Call the weather function and store the result in weatherAlert
weatherAlert = weather()

# Function to determine vehicle response based on the weather condition
def vehicleResponseSystem():
    if weatherAlert == "snowing":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " it is", weatherAlert, "right now.")
        sleep(1)
        print("VRS has been engaged only allowing us yo drive 45MPH")
    elif weatherAlert == "blizzarding":
        print("\nThe National Weather Service has updated our alarm by 60 minutes because"
              " it is", weatherAlert, "right now.")
        sleep(1)
        print("VRS has been engaged only allowing you drive 30MPH")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 90 minutes because"
              " it is", weatherAlert, "right now.")
        sleep(1)
        print("VRS has been engaged only allowing you drive 25MPH")
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " it is", weatherAlert, "right now.")
        sleep(1)
        print("VRS has been engaged only allowing you drive 50MPH")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " it is", weatherAlert, "right now.")
        sleep(1)
        print("VRS has been engaged only allowing you drive 70MPH")
    else:
        # Default case for "sunny" or any other unexpected weather condition
        print("\nThe weather is", weatherAlert, "outside. Drive safe!")
        sleep(1)
        print("VRS has been disengaged drive safely!")

# Call the function to execute the weather alert system
vehicleResponseSystem()
