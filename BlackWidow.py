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
print(GREEN + "Welcome Branch - Developer: KB Manzini" + RESET)
print(YELLOW + "\nWelcome to InfoTechCenter v1.0" + RESET)

# Initialize variables for the boot animation
x = 0  # Counter for loop iterations
ellipsis = 0  # Counter for the number of dots in the boot message

# Boot-up animation loop
while x != 20:  # Loop runs 20 times to simulate loading
    x += 1  # Increment loop counter
    message = (CYAN + "Infotech Center System Booting" + "." * ellipsis + RESET)  # Create boot message with dots
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