def handle_multiple_exceptions(a, b):
    try:
        result = a / b
        my_list = [1, 2, 3]
        print(my_list[5])  
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    except IndexError as e:
        print(f"IndexError: {e}")
    except Exception as e:
        print(f"Some other error: {e}")


handle_multiple_exceptions(10, 0)
