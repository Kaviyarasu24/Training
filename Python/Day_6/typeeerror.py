def add_numbers(a, b):
    try:
        return a + b
    except TypeError as e:
        print(f"Error: {e}")

add_numbers("hello", 5)  