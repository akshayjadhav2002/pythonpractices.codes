
def outer():
    count =0
    def inner ():
        print(count)
        nonlocal count
        count += 1
        return count
    return inner
if __name__ == "__main__":
    counter = outer()
    print(counter())
    print(counter())

# nonlocal =  nested function cha outside  che inner function la disat nai so tay sathi nonlocal key  word use kartat