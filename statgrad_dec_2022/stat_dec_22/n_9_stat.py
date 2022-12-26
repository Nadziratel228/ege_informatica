def main():
    s = open('n_9_stat.txt','r').readlines()
    k = 0   
    for i in s: 
        n = sorted( int(x) for x in i.split() )
        kodd = 0
        keven = 0 
        sum_odd = 0 
        sum_even = 0 
        for j in n:
            if j%2 == 0:
                keven += 1
                sum_even += j 
            else:
                kodd += 1
                sum_odd += j
        if n[0] != n[1] and n[1] != n[2] and n[2] != n[3] and n[3] != n[4] and keven > kodd and sum_even < sum_odd:
            k += 1
    return k
print(main())
