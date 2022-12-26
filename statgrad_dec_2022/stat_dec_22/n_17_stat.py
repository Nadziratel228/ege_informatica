def main():
    s = open('n_17_stat.txt','r').readlines()
    s = [int(x) for x in s]

    mn = 10000000
    for i in s:
        if i%10 == 5:
            mn = min(i,mn)
    mn = mn * mn 

    k = 0
    mx = 0 
    for i in range(len(s)-1):
        if min(s[i],s[i+1])%10 == 5 and (s[i]*s[i] + s[i+1]*s[i+1]) < mn:
            k = k + 1 
            mx = max(mx,s[i]*s[i] + s[i+1]*s[i+1])
    return k,mx
print(*main())