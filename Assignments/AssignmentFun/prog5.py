rate = [2, 4, 5, 6, 2, 2, 7, 8, 2, 9, 10, 11]
cnt = 0

def countSearch(rate, x):
    for i in rate:
        if i == x:
            global cnt
            cnt += 1
    return cnt

x = int(input("Enter the number to search: "))
ans = countSearch(rate, x)
print(ans)
