def persistence(n):
    x = str(n)
    count = 0

    while len(x) > 1:
        total = 1

        for digit in x:
            total *= int(digit)

        x = str(total)
        count += 1

    print(count)  
        
persistence(4)