def f():
    s = open('n_24_stat.txt','r').readlines()

    l = list()
    for i in s:
        raz, tip = i.split()
        l.append([int(raz),tip])

    l.sort(reverse = True)

    k = [[l[0]]]

    for i in l[1:]:
        new_block = True 
        for j in k:
            if j[-1][0] - i[0] >= 5 and i[1] != j[-1][1]:
                j.append(i)
                new_block = False 
                break
        if new_block:
            k.append([i])

    return max(len(x) for x in k),len(k)
print(*f())