try:
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except UnicodeDecodeError:
    print("Error: The file contains characters that cannot be decoded using the specified encoding.")
