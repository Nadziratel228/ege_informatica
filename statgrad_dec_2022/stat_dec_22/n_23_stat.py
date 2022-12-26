def f():
    from fnmatch import fnmatch
    for i in range(0,10**9+1,3123):
        if fnmatch(str(i),'12*63?5?'):
            print(i)
    return 
f()