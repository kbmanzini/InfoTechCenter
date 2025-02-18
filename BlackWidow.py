import random
from time import sleep

# Print initial information about the program
print("\n**********************\n")
print("Gasoline Branch - Developer:KB Manzini")

# Function to randomly select a gas level
def gasLevelGauge():
    # List of possible gas levels
    gasLevelList = ['Empty', 'low', 'quarter tank', 'half tank', 'three quarter tank', 'full tank']
    return random.choice(gasLevelList)  # Randomly choose a gas level from the list

# Function to randomly select a gas station
def gasStations():
    # List of possible gas stations
    gasStationsList = ['Shell', 'Marathon', 'Speedway', 'Circle K', 'Wesco', 'Meijer', 'Buc-ees']
    return random.choice(gasStationsList)  # Randomly choose a gas station

# Function to determine how far the nearest gas station is based on the current gas level
def getMilesToGasStation(gasLevelIndicator):
    # Return miles to nearest gas station based on the gas level
    if gasLevelIndicator == "Empty":
        return round(random.uniform(0, 5), 1)  # For "Empty", gas station is very close (0-5 miles)
    elif gasLevelIndicator == 'low':
        return round(random.uniform(1, 25), 1)  # For "low", the station is 1-25 miles away
    elif gasLevelIndicator == 'quarter tank':
        return round(random.uniform(25.1, 50), 1)  # For "quarter tank", the station is 25-50 miles away
    else:
        return round(random.uniform(50.1, 100), 1)  # For "half tank", "three quarter tank", and "full tank", stations are further away (50-100 miles)

# Main function to handle gas level alerts and find nearest gas stations
def gasLevelAlert():
    # Get the current gas level and corresponding miles to nearest station
    gasLevelIndicator = gasLevelGauge()  # Call the gasLevelGauge function to get a random gas level
    milesToGastStation = getMilesToGasStation(gasLevelIndicator)  # Get the distance to the nearest gas station

    # Check the gas level and provide the appropriate alert and nearest gas station info
    if gasLevelIndicator == "Empty":
        print("*** WARNING - YOU ARE OUT OF GAS ***\n")  # Warning message for empty gas tank
        sleep(1.25)  # Simulate a delay before next action
        print("Calling AAA")  # Simulate calling AAA for help
    elif gasLevelIndicator in ['low', 'quarter tank', 'half tank', 'three quarter tank']:
        # If the gas level is low, quarter tank, half tank, or three quarter tank, show gas station info
        print(f"Your gas tank is {gasLevelIndicator}, checking GPS for the closest gas station")
        sleep(1.25)  # Simulate a delay
        print(f"The closest gas station is {gasStations()}, which is {milesToGastStation} miles away.")  # Display the closest gas station and distance
    else:
        # If the tank is full, no need to worry about refueling
        print("Your gas tank is full, drive safely!")  # Message for full tank

# Call the function to trigger the alert and gas station search
gasLevelAlert()
