def main():
    choice = int(input("Matrix Operations Menu\n1. Find the transpose of a 4x4 matrix\n2. To terminate the program\nEnter your choice (1/2): "))
    if choice == 1:
        arr = [[0 for _ in range(4)] for _ in range(4)]
        print("Enter a 4x4 matrix:")
        for i in range(4):
            for j in range(4):
                arr[i][j] = int(input(f"Enter the element at row {i + 1}, column {j + 1}: "))
        print("The entered matrix is as follows:")
        for i in range(4):
            for j in range(4):
                print(arr[i][j], end=" ")
            print()
        print("The transpose of the matrix is:")
        for i in range(4):
            for j in range(4):
                print(arr[j][i], end=" ")
            print()
    elif choice == 2:
        exit(0)
    else:
        print("Invalid choice. Please select either 1 or 2.")

if __name__ == "__main__":
    main()