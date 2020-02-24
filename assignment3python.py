def maxconsecutiveOnes(y):
    c=0
    while (y!=0):
        y=(y & (y <<1))
        c+=1
    return c
print(maxconsecutiveOnes(int(input())))

