from collections import Counter
def most_frequent_char(string):
    frequency = Counter(string)
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent
string = input("Enter the string: ")
result = most_frequent_char(string)
print(f"The most frequent character is: {result}")