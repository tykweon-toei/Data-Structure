def hanoi(n, fm, tmp, to):

    if n==1:
        print("Move plate From " + str(fm) + " To " + str(to))
    else:
        hanoi(n-1, fm, to, tmp)
        print("Move plate number " + str(n) + " From " + str(fm) + " To " + str(to))
        hanoi(n-1, tmp, fm, to)


num= int(input("Input Number : "))

hanoi(num, 'A', 'B', 'C')