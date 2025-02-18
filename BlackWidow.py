import random
from time import sleep

# Print header information
print("\n**********************\n")
print("Gasoline Branch - Developer:KB Manzini")


# Function to randomly select a gas level
def gasLevelGauge():
    # List of possible gas levels
    gasLevelList = ['Empty', 'low', 'quarter tank', 'half tank', 'three quarter tank', 'full tank']
    return random.choice(gasLevelList)  # Randomly select and return a gas level from the list


# Function to randomly select a gas station
def gasStations():
    # List of possible gas stations
    gasStationsList = ['Shell', 'Marathon', 'Speedway', 'Circle K', 'Wesco', 'Meijer', 'Buc-ees']
    return random.choice(gasStationsList)  # Randomly select and return a gas station from the list


# Function to determine the number of miles to the nearest gas station based on the current gas level
def getMilesToGasStation(gasLevelIndicator):
    # Return miles to the nearest gas station based on the current gas level
    if gasLevelIndicator == "Empty":
        return round(random.uniform(0, 5), 1)  # If gas is empty, the station is very close (0-5 miles)
    elif gasLevelIndicator == 'low':
        return round(random.uniform(1, 25), 1)  # If gas is low, the station is 1-25 miles away
    elif gasLevelIndicator == 'quarter tank':
        return round(random.uniform(25.1, 50), 1)  # If gas is a quarter tank, the station is 25-50 miles away
    else:
        return round(random.uniform(50.1, 100),
                     1)  # For higher gas levels (half tank, three quarter tank, full tank), stations are further (50-100 miles)


# Main function to check the gas level and alert the user with gas station info
def gasLevelAlert():
    # Get the current gas level by calling gasLevelGauge() function
    gasLevelIndicator = gasLevelGauge()

    # Get the number of miles to the nearest gas station based on the gas level
    milesToGastStation = getMilesToGasStation(gasLevelIndicator)

    # Check if the gas level is "Empty"
    if gasLevelIndicator == "Empty":
        print("*** WARNING - YOU ARE OUT OF GAS ***\n")  # Display warning for empty tank
        sleep(1.25)  # Simulate a short pause before next action
        print("Calling AAA")  # Simulate calling AAA for roadside assistance

    # Check if the gas level is low, quarter tank, half tank, or three quarter tank
    elif gasLevelIndicator in ['low', 'quarter tank', 'half tank', 'three quarter tank']:
        print(
            f"Your gas tank is {gasLevelIndicator}, checking GPS for the closest gas station")  # Inform the user about their current gas level
        sleep(1.25)  # Simulate a short pause before next action
        # Display the closest gas station and how far away it is
        print(f"The closest gas station is {gasStations()}, which is {milesToGastStation} miles away.")

    # If the gas tank is full, display a message indicating no need to worry
    else:
        print("Your gas tank is full, drive safely!")  # Inform the user that the tank is full and they can drive safely

# Call
