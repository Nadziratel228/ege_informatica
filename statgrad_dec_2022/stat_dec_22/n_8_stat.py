def f():
    k = 0
    from itertools import product 
    for i in product('ВЕРОНИКА',repeat = 6):
        if i.count('Е') + i.count('О') + i.count('И') + i.count('А') > i.count('В') + i.count('Р') + i.count('Н') + i.count('К'):
            k += 1 
    return k 
print(f())