import random
l= []
for i in range(4):
    l.append(random.randint(-10,10))
print(l)

pr = 1

def Dpr(x):
    global pr
    if x == len(l):
        return
    pr *= l[x]
    Dpr(x + 1)

Dpr(0)
print('\nПроизведение = ', pr)
