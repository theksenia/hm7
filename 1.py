b= int(input("Enter: "))

def sum(x):
    if x > 0:
        return sum(x // 10) + x % 10
    else:
        return 0
print(sum(b))