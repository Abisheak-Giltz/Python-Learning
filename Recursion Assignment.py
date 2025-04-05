
# recursion function for power

def powerOf(x, y) :
    if y == 0 :
        return 1
    else :
        return x * powerOf(x, (y - 1))

print(powerOf(2, 4))
