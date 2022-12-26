for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (bool(x) != (not(y))) or ((not(z) or not(w)) and (not(w) or y)):
                    print(x,y,w,z)
print('False:')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((bool(x) != (not(y))) or ((not(z) or not(w)) and (not(w) or y))):
                    print(x,y,w,z)

    