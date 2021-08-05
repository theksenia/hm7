n= int(input("Enter: "))
def correct(x):
    i = 1
    p = False
    while i < x:
        i = i * 2
    if i == x:
        p = True
    else:
        p = False
    return p
print (correct(n))