def outer():
    message = " i am the outer function "
    def inner():
        return message
    return inner

if __name__ == "__main__":
    inner_function = outer()
    result = inner_function()
    print(result)