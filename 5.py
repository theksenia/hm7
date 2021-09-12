def outer(a,b):
    def inner(a,b):
        global x
        x = a+b
        return x
    global x
    inner(a, b)
    x = x+5
    return x

print(outer(8,15))

