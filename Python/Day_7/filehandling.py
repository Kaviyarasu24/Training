def read_file_to_array(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines

file_path = 'example.txt'
lines_array = read_file_to_array(file_path)
print(lines_array)