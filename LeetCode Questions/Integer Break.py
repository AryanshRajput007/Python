n = int(input("Enter a Number: "))

if n == 2:
    print(1)
elif n == 3:
    print(2)
else:
    count = n // 3
    remainder = n % 3

    if remainder == 0:
        print(int(3 ** count))
    elif remainder == 1:
        print(int((3 ** (count - 1)) * 4))
    else:
        print(int((3 ** count) * 2))
