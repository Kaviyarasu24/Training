def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Error: {e}")


open_file("non_existent_file.txt")  