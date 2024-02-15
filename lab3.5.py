x = int(input("Enter a number of repetitions: "))

def hello_repeat(repetitions):
    def decorator(func):
        def wrapper():
            for _ in range(repetitions):
                func()
        return wrapper
    return decorator

@hello_repeat(x)
def hello():
    print('Hello')

hello()