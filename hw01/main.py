for row in range(1,10):
    print(end="       "*(row-1))
    for col in range(row,10):
        print("{0}x{1}={2:<2}".format(row,col,row*col),end=" ")
    print()
