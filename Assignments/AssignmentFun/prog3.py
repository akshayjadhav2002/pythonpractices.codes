arr = [2,4,6,8,10]

def factorial(arr):
    for i in arr:
        fact = i *(i-1)
    return fact

ans = factorial(arr)
print(ans)