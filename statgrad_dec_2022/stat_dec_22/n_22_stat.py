def f():
    s = open('n_22_stat.txt','r').readline().split('D')
    k = 1
    mx = -1
    for i in s:
        if i.count('O')<=2:
            k += len(i) + 1
        else:
            mx = max(k,mx)
            k = 1
    return mx
print(f())