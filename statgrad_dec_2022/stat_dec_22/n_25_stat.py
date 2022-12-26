def st_3(n):
    k = 0
    while (n % 3 == 0):
        k += 1 
        n //= 3
    return int(k)

def zapolnenie(a,s):
    for i in s: a[st_3(i)][i%4] +=1

    return a 

def answer(a):
    s = 0
    for i in range(len(a)):
        for j in range(i,len(a)):
            for k in range(4):
                if i + j >= 8 and i == j and (k == 0 or k == 2):
                    s += (a[i][k]*(a[i][k]-1))//2
                elif i + j >=8 and i == j and k == 3:
                    break 
                elif i + j >=8:
                    s += a[i][k]*a[j][(4-k)%4]
    return s 

def main_A():
    a = [[0]*4 for i in range(12)]
    s = open('n_25_stat_A.txt','r').readlines()
    s = [int(x) for x in s]
    
    return answer(zapolnenie(a,s)) 
    

def main_B():
    a = [[0]*4 for i in range(12)]
    s = open('n_25_stat_B.txt','r').readlines()
    s = [int(x) for x in s]

    return answer(zapolnenie(a,s))

print(main_A(),main_B())
