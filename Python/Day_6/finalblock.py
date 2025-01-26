def example_finally_block():
    try:
        print("Inside try block")
        result = 10 / 2  
    except ZeroDivisionError:
        print("Inside except block")
    finally:
        print("This is the finally block - always executes.")


example_finally_block()
