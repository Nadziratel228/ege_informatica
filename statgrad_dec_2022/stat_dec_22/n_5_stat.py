def f(n):
    a = 0
    while n > 0:
        a += n%10
        n //= 10 
    if a%2==0:
        return True 
    else: 
        return False
def ans():
    mn = 1000000
    for i in range(0,100000):
        s = bin(i)[2:]
        for k in range(3):
            if f(int(s,2)):
                s = s + '0'
            else:
                s = s + '1'
        if int(s,2) > 1028:
            mn = min(int(s,2),mn)
    return mn 
print(ans())