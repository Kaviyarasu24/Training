row, col = input("Enter number of rows and columns: ").split()
row = int(row)
col = int(col)
print("Hollow square pattern is: ")
for i in range(1, row + 1):
    for j in range(1, col + 1):
            if i == 1 or i == row or j == 1 or j == col:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()