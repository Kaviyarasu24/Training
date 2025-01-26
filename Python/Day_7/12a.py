def count_word_frequency(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    
    words = text.split()
    frequency = {}
    
    for word in words:
        word = word.lower().strip('.,!?";:')
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

file_path = 'example.txt'
word_frequency = count_word_frequency(file_path)
for word, count in word_frequency.items():
    print(f"{word}: {count}")