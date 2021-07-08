# python provides a generator to create your own iterator function
# In a generator function, a yield statement is used rather than a return statement.

# Example?:

def myGenerator():
    print('first item')
    yield 10

    print('second item')
    yield 20

    print('Last item')
    yield 30

gen = myGenerator()

def fibonacci(max):
    a, b = 0, 1
    while a < max:
        print(a, ',', b)
        yield a
        a, b = b, a+b


# k = 10
f = fibonacci(10)
# next(f)

# def run(x):
for i in range(7):
    # yield i
    # print(next(f))
    # print(next(f))
    # next(gen)
    next(f)


# run(3)