a = input()
a = str(a)
result = 0
count = 0
def summa_cifr(a, count, result):
    c = ''
    c = c + a[count]
    c = int(c)
    result = result + c
    if count < len(a):
        return summa_cifr(a,count+1, result)
    else:
        return result
summa_cifr(a, count, result)
print(result)
