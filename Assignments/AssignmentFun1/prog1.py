def outer ():
    def inner():
        return "hello I Am in Inner function"
    return inner()

ans = outer ()
print(ans)