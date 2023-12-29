import os

def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

while True:
    print("Press 1 to calculate the area and perimeter of a rectangle.")
    print("Press 2 to exit.")

    choice = input("Enter your choice: ")

    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        area, perimeter = rectangle_properties(length, width)

        print(f"The area of the rectangle is: {area}")
        print(f"The perimeter of the rectangle is: {perimeter}")
    elif choice == '2':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")

    user_input = input("Do you want to perform another operation? (yes/no): ")

    if user_input.lower() != 'yes':
        print("Exiting the program. Goodbye!")
        break

    os.system('cls' if os.name == 'nt' else 'clear')