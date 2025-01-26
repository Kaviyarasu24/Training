def capitalize_first_letter_of_each_word(sentence):
    return sentence.title()
sentence = input("Enter string: ")
result = capitalize_first_letter_of_each_word(sentence)
print(f"Capitalized sentence: {result}")
