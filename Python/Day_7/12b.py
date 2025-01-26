def remove_newlines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line.replace('\n', ''))
filename = 'example.txt'
remove_newlines(filename)