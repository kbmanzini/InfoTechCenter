import sys  # Importing system module to manipulate output
from time import sleep  # Importing sleep function to create a delay

# VS Code color theme compatibility using ANSI escape codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"  # Reset color

# Display welcome message with developer name
print(RED + "Welcome Branch - Developer: KB Manzini" + RESET)
print(MAGENTA + "\nWelcome to InfoTechCenter v1.0" + RESET)

# Initialize variables for the boot animation
x = 0  # Counter for loop iterations
ellipsis = 0  # Counter for the number of dots in the boot message

# Boot-up animation loop
while x != 20:  # Loop runs 20 times to simulate loading
    x += 1  # Increment loop counter
    message = (RED + "Infotech Center System Booting" + "." * ellipsis + RESET)  # Create boot message with dots
    ellipsis += 1  # Increase dot count
    
    # Overwrite the same line with the updated message
    sys.stdout.write("\r" + message)
    sys.stdout.flush()  # Ensure the output updates in real-time
    
    sleep(0.5)  # Pause for half a second to create animation effect
    
    # Reset dot count after three dots to cycle animation
    if ellipsis == 4:
        ellipsis = 0
    
    # End the loop when counter reaches 20
    if x == 20:
        print(MAGENTA + "\n\nOperating System Booted Up - Retina Scanned - Access Granted\n" + RESET)  # Final message

import random  # Used to generate random weather conditions

# Print a decorative header
print("\n****************************\n")
print("Weather Branch - Developer: KB Manzini")


# Function to determine the weather condition randomly
def weather():
    weather_forcast_list = ["snowing", "blizzarding", "icy", "rainy", "windy", "sunny"]
    return random.choice(weather_forcast_list)  # Randomly select a weather condition


# Call the weather function and store the result in weatherAlert
weather_alert = weather()

# Dictionary to map weather conditions to alarm times and speed limits
weather_info = {
    "snowing": {"alarm_time": 30, "speed_limit": 45},
    "blizzarding": {"alarm_time": 60, "speed_limit": 30},
    "icy": {"alarm_time": 90, "speed_limit": 25},
    "rainy": {"alarm_time": 5, "speed_limit": 50},
    "windy": {"alarm_time": 5, "speed_limit": 70},
    "sunny": {"alarm_time": 0, "speed_limit": 75},  # Default for sunny
}


# Function to determine vehicle response based on the weather condition
def vehicle_response_system():
    # Fetch weather information from the dictionary
    weather_data = weather_info.get(weather_alert, {"alarm_time": 0, "speed_limit": 75})

    # Display the alarm update
    if weather_data["alarm_time"]:
        print(
            f"\nThe National Weather Service has updated our alarm by {weather_data['alarm_time']} minutes because it is {weather_alert} right now.")
        print(f"\nVRS has been engaged only allowing you to drive {weather_data['speed_limit']} MPH")
    else:
        print(f"\nThe weather is {weather_alert} outside. Drive safe!")
        print("VRS has been disengaged. Drive safely!")


# Call the function to execute the weather alert system
vehicle_response_system()