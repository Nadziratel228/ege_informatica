def f(n,a,b):
    if n == 14:
        return 1 
    if n > 14:
        return 0 
    if a == 2:
        return f(n*2,0,1)
    if b == 2:
        return f(n+1,1,0)
    return f(n+1,a+1,0) + f(n*2,0,b+1)
print(f(1,0,0))