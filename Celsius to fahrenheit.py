def calculator(choice):
  if choice == 1:
    celsius = float(input("Enter celsius value: "))
    fahrenheit = (celsius * 9/5) + 32
    print("The celsius value in fahrenheit is: ", fahrenheit)
  elif choice == 2:
    fahrenheit = float(input("Enter fahrenheit value: "))
    celsius = (fahrenheit - 32) * 5/9
    print("The fahrenheit value in celsius is: ", celsius)
  else:
    print("Invalid choice")

choice = int(input("Press 1 to enter celsius value and 2 to enter fahrenheit value: "))
calculator(choice)