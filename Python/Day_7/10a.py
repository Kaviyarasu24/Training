try:
    user_input = input("Please enter a number: ")

    print(f"You entered: {user_input}")

except KeyboardInterrupt:
    print("\nInput was cancelled. Exiting the program.")
