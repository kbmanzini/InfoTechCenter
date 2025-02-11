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
        print(f"VRS has been engaged only allowing you to drive {weather_data['speed_limit']} MPH")
    else:
        print(f"\nThe weather is {weather_alert} outside. Drive safe!")
        print("VRS has been disengaged. Drive safely!")


# Call the function to execute the weather alert system
vehicle_response_system()
