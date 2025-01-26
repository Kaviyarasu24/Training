def replace_substring(original_string, old_substring, new_substring):
    return original_string.replace(old_substring, new_substring)
original_string =input("string: ")
old_substring = input("old substring: ")
new_substring = input("new substring: ")
result = replace_substring(original_string, old_substring, new_substring)
print(f"Modified string: {result}")