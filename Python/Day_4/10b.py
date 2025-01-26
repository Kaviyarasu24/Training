from collections import Counter
def second_most_frequent_char(s):
    freq = Counter(s)
    common_chars = freq.most_common()
    if len(common_chars) < 2:
        return None
    return common_chars[1][0]
input_string = input("Enter string: ")
result = second_most_frequent_char(input_string)
print(result)