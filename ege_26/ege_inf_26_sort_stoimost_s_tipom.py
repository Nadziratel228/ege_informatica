def main():
    s = sorted([i.split() for i in open('1.txt','r').readlines()], key = lambda x:int(x[0]))
    sm = 100_000
    lst = []
    for i in [j for j in s]: 
        if sm - int(i[0]) < 0: break
        else: 
            sm -= int(i[0])
            lst.append(i)
            s.remove(i)
    lst.sort(key = lambda x:int(x[0]), reverse = True)
    for i in [i for i in lst]:
        if i[1] == 'Q':
            for j in [j for j in s]:
                if sm - (int(j[0])-int(i[0])) < 0: break
                if j[1] == 'Z':
                    sm -= (int(j[0]) - int(i[0]))
                    lst.remove(i)
                    s.remove(j)
                    lst.append(j)
                    break 
    return sum(1 for i in lst if i[1] == 'Z'),sm

print(*main())