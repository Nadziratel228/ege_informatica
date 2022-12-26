from functools import lru_cache
def m(s):
    if s[0] < s[1]: 
        return (s[0]+1,s[1]),(s[0]+2,s[1]),(s[0]*2,s[1])
    elif s[0] == s[1]:
         return (s[0]+1,s[1]),(s[0]+2,s[1]),(s[0]*2,s[1]),(s[0],s[1]+1),(s[0],s[1]+2),(s[0],s[1]*2)
    else:
        return (s[0],s[1]+1),(s[0],s[1]+2),(s[0],s[1]*2)
    
@lru_cache(None)
def game(s):
    if s[0] + s[1] >=81:
        return 'w'
    
    if any(game(move)=='w' for move in m(s)):
        return 'p1'
    if all(game(move)=='p1' for move in m(s)):
        return 'v1'
    if any(game(move)=='v1' for move in m(s)):
        return 'p2'
    if all(game(move) == 'p1' or game(move) == 'p2' for move in m(s)):
        return 's3'

s1 = []
s2 = []
s3 = []
for i in range(1,69):
    if game((12,i)) == 'v1':
        s1.append(i)
    if game((12,i)) == 'p2': 
        s2.append(i)
    if game((12,i)) == 's3':
        s3.append(i)

print(s1[0])
print(s2[0],s2[-1])
print(s3[-1])
    