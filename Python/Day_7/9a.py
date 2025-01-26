try:
    user_input = input("Please enter an integer: ")
    num = int(user_input)
    print(f"You entered the integer: {num}")
except ValueError:
    print("Error: The input is not a valid integer. Please enter an integer.")
