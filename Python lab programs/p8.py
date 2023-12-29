import os

def ascender(lst):
    lst.sort()
    return lst

def descender(lst):
    lst.sort(reverse=True)
    return lst

while True:
    choice = input("Select an Option\nPress 1 to arrange the list in Ascending order\nPress 2 to arrange the list in Descending order\nPress 3 to exit\nEnter your choice: ")

    if choice == '1':
        my_list = [int(x) for x in input("Enter the values separated by spaces: ").split()]
        my_list = ascender(my_list.copy())
        print("The list in Ascending order is:", my_list)
    elif choice == '2':
        my_list = [int(x) for x in input("Enter the values separated by spaces: ").split()]
        my_list = descender(my_list.copy())
        print("The list in Descending order is:", my_list)
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
