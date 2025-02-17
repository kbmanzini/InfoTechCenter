import random
from time import sleep

print("\n**********************\n")
print("Gasoline Branch - Developer:KB Manzini")

def gasLevelGauge():
    gasLevelList = ['Empty' , 'low' , 'quarter tank' , 'half tank' , 'three quarter tank' 'full tank']
    return random.choice(gasLevelList)



def gasStations(): 
    gasStationsList = ['Shell' , 'Marathon' , 'Speedway' , 'Circle K' , 'Wesco' , 'Meijer' , 'Buc-ees']
    return random.choice(gasStationsList)
    
    
def gasLevelAlert():
        milesToGastStationLow = round(random.uniform(1,25),1)
        milesToGastStationQuarterTank = round(random.uniform(25.1,50),1)
        gasLevelIndicator = gasLevelGauge()
        if gasLevelIndicator == "Empty":
            print("*** WARNING - YOUR ARE OUT OF GAS***\n")
            sleep(1.25)
            print("Calling AAA")
        elif gasLevelIndicator == 'Low':
            print('Your gas tank is extremely low, checking GPS for the closes gas station')
            sleep(1.25)
            print("The closest gas station is" , gasStations(), 'which is', milesToGastStationLow, 'miles away.')
        elif gasLevelIndicator == 'Quarter Tank':
            print('Your gas tank has a quarter left, checking GPS for the closes gas station')
            sleep(1.25)
            print("The closest gas station is" , gasStations(), 'which is', milesToGastStationQuarterTank,'miles away.')
        
gasLevelAlert()
