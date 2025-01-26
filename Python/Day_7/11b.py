try:
    my_list = [1, 2, 3, 4, 5]
    my_list.add(6)

except AttributeError:
    print("Error: 'list' object has no attribute 'add'. Use 'append' instead.")
