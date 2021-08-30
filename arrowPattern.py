#Arrow pattern

columns = 8
for x in range(columns):
    if (x < (columns // 2)):
        print(" " * x + "*")
    else:
        print(" " * (-x + (columns - 1)) + "*")