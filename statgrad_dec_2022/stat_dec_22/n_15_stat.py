def f():
    for a in range(0,1000):
        k = 0 
        for x in range(1,1001):
            for y in range(1,1001):
                if 108 % x != 0 or x % y != 0 or x + y > 80 or a - y > x:
                    k += 1
        if  k == 10**6:
            return a 
        k = 0
    return 0
print(f())
