def main():
    s = [[int(x) for x in i.split('.')] for i in open('1.txt','r').readlines()]
    mask = [255,255,224,0]
    ans2 = []
    d = {}
    for i in s: 
        f = ''
        for j in range(4): f += str(mask[j]&i[j])
        f = int(f)
        if f in d: d[f] += 1
        else: d[f] = 1 

    ans1 = max(d.items(), key=lambda x: x[1])[0]


    for i in s:
        f = ''
        for j in range(4): f += str(mask[j]&i[j])
        f = int(f)
        if f == ans1:
            st = ''
            for j in range(4): st += str(i[j])
            ans2.append(int(st))
    return ans1, len(set(ans2))
print(*main())