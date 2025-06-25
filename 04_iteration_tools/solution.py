def decorator(func):
    def wrapper():
        print("before calling the function")
        func()
        print("after calling the function")
    return wrapper
@decorator
def greet():
    print("hello","world!")
greet()
