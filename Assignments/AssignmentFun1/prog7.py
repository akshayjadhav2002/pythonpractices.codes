def outer():
    def inner():
        return "hello, core2web"
    return inner
    print("In outer Func")

if __name__ == "__main__":
    result = outer()
    # innernally it call like result()
    print(result)