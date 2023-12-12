def find_next_permutation(num):
    num_list = list(str(num))

    # Find the first decreasing digit from the right
    i = len(num_list) - 2
    while i >= 0 and num_list[i] >= num_list[i+1]:
        i -= 1

    # If no such digit is found, it's not possible
    if i == -1:
        return "Not Possible"

    # Find the smallest digit to the right of i but greater than num_list[i]
    j = len(num_list) - 1
    while num_list[j] <= num_list[i]:
        j -= 1

    # Swap the two digits
    num_list[i], num_list[j] = num_list[j], num_list[i]

    # Reverse the digits to the right of i
    num_list[i+1:] = num_list[i+1:][::-1]

    next_permutation = int(''.join(num_list))
    return next_permutation

# Example usage:
given_number = 123
result = find_next_permutation(given_number)
print("Smallest number with the same set of digits:", result)
