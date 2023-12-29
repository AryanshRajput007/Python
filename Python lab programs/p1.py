import os

def calculator(choice):
    if choice == 1:
        celsius = float(input("Enter Celsius value: "))
        fahrenheit = (celsius * 9/5) + 32
        print("The Celsius value in Fahrenheit is: ", fahrenheit)
    elif choice == 2:
        fahrenheit = float(input("Enter Fahrenheit value: "))
        celsius = (fahrenheit - 32) * 5/9
        print("The Fahrenheit value in Celsius is: ", celsius)
    else:
        print("Invalid choice")

while True:
    choice = int(input("Press 1 to enter Celsius value \nPress 2 to enter Fahrenheit value \nPress 3 to exit\nEnter your choice: "))

    if choice == 3:
        print("Exiting the calculator. Goodbye!")
        break
    elif choice in [1, 2]:
        calculator(choice)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear') 
