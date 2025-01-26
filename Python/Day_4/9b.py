def remove_duplicates(string):
    result = ''
    for char in string:
        if char not in result:
            result += char
    return result
string =input("Enter string: ")
result = remove_duplicates(string)
print(f"String without duplicates: {result}")