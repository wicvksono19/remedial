def multiplication_table(x,y):
    for j in range(1, x+1):
        for i in range(1, y+1):
            print("{:4}".format (i * j), end = '')
        print("")


multiplication_table(3,3)