def outer():
    def inner():
        return "Hello I'm the inner function"
    return inner()
ans = outer()
print(ans)