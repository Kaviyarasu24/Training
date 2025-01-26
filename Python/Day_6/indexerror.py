def access_element(my_list, index):
    try:
        return my_list[index]
    except IndexError as e:
        print(f"Error: {e}")
access_element([1, 2, 3], 5) 
