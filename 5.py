a = int(input("Enter: "))
b = int(input("Enter: "))
def sum(a,b):
    def pro(x):
        x= a+b
    global x
    x= x+5
    return x
print(sum(a,b))