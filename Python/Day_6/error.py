def exception_handling_demo():
    try:
 
        num = int(input("Enter a number: "))
        result = 10 / num
        print(f"Result: {result}")


        data = {'name': 'Alice'}
        print(f"Age: {data.get('age', 'Age not found')}")  


        numbers = [1, 2, 3, 4]  
        print(f"Fourth number: {numbers[5]}")

    except ZeroDivisionError as e:
        print(f"Error: Cannot divide by zero. {e}")
    except KeyError as e:
        print(f"Error: Missing key in dictionary. {e}")
    except IndexError as e:
        print(f"Error: Index out of range. {e}")
    except ValueError as e:
        print(f"Error: Invalid input. Please enter a valid number. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("All operations executed successfully without any errors.")
    finally:
        print("Execution of the try-except block is complete.")

exception_handling_demo()
