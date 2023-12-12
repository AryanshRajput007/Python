import numpy as np

# Ask the user for the size of the array
array_size = int(input("Enter the size of the array: "))

# Initialize an empty list to store user input
user_input_list = []

# Collect user input and append it to the list
for i in range(array_size):
    element = int(input("Enter element " + str(i + 1) + ": "))
    user_input_list.append(element)

# Convert the list to a NumPy array
user_input_array = np.array(user_input_list)

# Print the resulting array
print("User input array:", user_input_array)
