b= int(input("Enter: "))

def sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

print(sum(b))