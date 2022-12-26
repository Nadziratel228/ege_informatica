def f(s):
    if len(s[0]) == 20: return s 
    a = list()
    for i in s:
        if i.count('1') < 10: a.append(i+'1')
        if i.count('2') < 10: a.append(i+'2')
    return f(a)
def ans():
    s = ['1','2']
    k = -10
    for i in f(s):
        if i.count('1') == 10:
                s = '0' + str(i) + '0'
                while '00' not in s:
                    s = s.replace('012','30',1)
                    if '011' in s:
                        s = s.replace('011','20',1)
                        s = s.replace('022','40',1)
                    else:
                        s = s.replace('01','10',1)
                        s = s.replace('02','101',1)
                if s.count('1') == 6 and s.count('2') == 5:
                    k = max(k,s.count('3'))
    return k 
print(ans())